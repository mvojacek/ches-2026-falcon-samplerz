`timescale 1ns/1ps

import fp_pkg::*;

// Combinational module - splits a POSITIVE or NEGATIVE floating point number into its fractional and integral parts
// Implements DecomposeZ algorithm: x = z + r, where z is integer, r in [0, 1)
// !! UNUSED IN THE FINAL DESIGN !!
// !! NOT THOROUGHLY TESTED !!
// !! DO NOT USE !!
module fp_int_frac_z #(
  parameter INT_W = 32
) (
  input  fp_t in, // IEEE double
  output fp_t out_frac, // IEEE double fractional part, [0,1)
  output logic [INT_W-1:0] out_int // integral part
);
  typedef logic [INT_W-1:0] int_t;

  // input decompose

  (* keep="soft" *) logic  sign;
  fp_exp_t  exp;
  fp_frac_t frac;
  assign {sign, exp, frac} = in;

  // float info decoding

  logic is_zero;
  assign is_zero = exp == 0; // send subnormals to zero (ignore frac)

  logic gte_one;
  assign gte_one = exp >= FP_EXP_BIAS;

  // barrel shift

  int signed exp_real_signed;
  assign exp_real_signed = int'(exp) - FP_EXP_BIAS;

  logic [INT_W-1+FP_FRAC_W:0] full_value;
  assign full_value = {{INT_W-1{1'b0}}, 1'b1, frac}; // add padding to the left of the fractional part

  // Unified shift logic
  fp_frac_t frac_shifted;
  int_t int_shifted;
  logic round_bit;
  logic sticky_rem;

  always_comb begin
    if (exp_real_signed >= 0) begin
       // Left shift
       logic [INT_W-1+FP_FRAC_W:0] shifted_lhs;
       shifted_lhs = full_value << exp_real_signed;
       
       frac_shifted = shifted_lhs[0+:FP_FRAC_W];
       int_shifted  = shifted_lhs[FP_FRAC_W+:INT_W];
       round_bit = 0;
       sticky_rem = 0;
    end else begin
       // Right shift
       // We use 64 bits of extra precision to catch lost bits
       logic [INT_W + FP_FRAC_W + 64 : 0] wide_in;
       logic [INT_W + FP_FRAC_W + 64 : 0] wide_shifted;
       
       wide_in = {full_value, 64'd0};
       wide_shifted = wide_in >> (-exp_real_signed);
       
       // Extract from the corresponding positions (shifted by 64)
       frac_shifted = wide_shifted[64 +: FP_FRAC_W];
       int_shifted  = wide_shifted[(64 + FP_FRAC_W) +: INT_W];
       
       round_bit  = wide_shifted[63];
       sticky_rem = |wide_shifted[0 +: 63];
    end
  end

  logic [FP_FRAC_W:0] r_raw; // 53 bits (MSB inclusive fractional result)
  logic [FP_FRAC_W:0] base;
  logic [FP_FRAC_W:0] frac_shifted_ext;

  always_comb begin
    base = 0;
    frac_shifted_ext = 0;
    if (!sign) begin
      // Positive: z = n, r = r'
      out_int = is_zero ? 0 : int_shifted;
      // frac_shifted is 52 bits. Extend to 53 (0 padded).
      r_raw   = is_zero ? 0 : {frac_shifted, 1'b0};
    end else begin
      // Negative
      if (is_zero) begin
        out_int = 0;
        r_raw   = 0;
      end else if (frac_shifted != 0 || round_bit != 0) begin
        // r' != 0: z = -n - 1, r = 1 - r'
        out_int = ~int_shifted;
        
        frac_shifted_ext = {frac_shifted, round_bit};
        base = -frac_shifted_ext;
        
        // Rounding Logic for 53-bit precision
        if (sticky_rem) begin
           // sticky_rem set -> True Value is Base - epsilon (epsilon < 0.5 ULP).
           // If Base[0] is 0: Value = Int - epsilon. Round to Int (Base).
           // If Base[0] is 1: Value = Half - epsilon (< 0.5). Round Down (Base - 1).
           if (base[0]) r_raw = base - 1'b1;
           else         r_raw = base;
        end else begin
           // sticky_rem clear -> True Value is Base exactly.
           // Since Base[0] represents 0.5 ULP in Double space.
           // If Base[0] is 0: Value is Exact Integer ULP. Keep Base.
           // If Base[0] is 1: Value is Exact Half ULP. Round to Nearest Even integer (Bit 1).
           if (base[0]) begin
              if (base[1]) r_raw = base + 1'b1; // Round Up to even
              else         r_raw = base - 1'b1; // Round Down to even
           end else begin
              r_raw = base;
           end
        end
        
      end else begin
        // r' almost 0 (only sticky_rem possibly set)
        out_int = -int_shifted;
        r_raw   = 0;
      end
    end
  end

  // count leading zeros on r_raw to normalize

  // Use WIDTH of 53
  logic [$clog2(FP_FRAC_W+1)-1:0] leading_zeros;

  lz_counter #(
    .WIDTH(FP_FRAC_W+1)
  ) lz_counter (
    .data_in(r_raw),
    .leading_zeros(leading_zeros)
  );

  logic out_raw_zero;
  assign out_raw_zero = leading_zeros == FP_FRAC_W + 1;

  // normalize float, including hidden bit

  logic [FP_FRAC_W:0] frac_norm_full;
  fp_frac_t frac_norm;
  
  // (r_raw << lz) aligns MSB (if set) to bit 52.
  assign frac_norm_full = (r_raw << leading_zeros);
  // Bit 52 is hidden. 51..0 are mantissa.
  assign frac_norm = frac_norm_full[FP_FRAC_W-1:0];

  fp_exp_t exp_norm;
  assign exp_norm = FP_EXP_BIAS - 1 - leading_zeros;

  // output out_frac

  always_comb begin
    if (is_zero) begin
      out_frac = 64'h0;
    end else if (!sign && !gte_one) begin
      // For positive small numbers, preserve original float (DecomposeN logic)
      out_frac = in; 
    end else if (out_raw_zero) begin
      out_frac = 64'h0; // zero fractional part (e.g. integer)
    end else begin
      out_frac = {1'b0, exp_norm, frac_norm}; // always positive [0, 1)
    end
  end

endmodule

module float_int_frac_z_registered #(
  parameter INT_W = 32
) (
  input clk,
  input fp_t in,
  output fp_t out_frac,
  output logic [INT_W-1:0] out_int
);

  fp_t _in, _out_frac;
  logic [INT_W-1:0] _out_int;
  always_ff @(posedge clk) begin
    _in <= in;
    out_frac <= _out_frac;
    out_int <= _out_int;
  end

  fp_int_frac_z #(
    .INT_W(INT_W)
  ) inst (
    .in(_in),
    .out_frac(_out_frac),
    .out_int(_out_int)
  );
endmodule
