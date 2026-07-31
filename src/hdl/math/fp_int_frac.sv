`timescale 1ns/1ps

import fp_pkg::*;

// Combinational module - splits a POSITIVE floating point number into its fractional and integral parts
module fp_int_frac #(
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

  logic gte_one;
  assign gte_one = exp >= FP_EXP_BIAS;

  fp_exp_t exp_real;
  assign exp_real = gte_one ? exp - FP_EXP_BIAS : 0;

  logic is_zero;
  assign is_zero = exp == 0; // send subnormals to zero (ignore frac)

  // barrel shift

  logic [INT_W-1+FP_FRAC_W:0] full_value, shifted_value;
  assign full_value = {{INT_W-1{1'b0}}, 1'b1, frac}; // add padding to the left of the fractional part
  assign shifted_value = full_value << exp_real; // shift right by the amount of the exponent

  fp_frac_t frac_shifted;
  int_t int_shifted;
  assign frac_shifted = shifted_value[0+:FP_FRAC_W]; // take the fractional part
  assign int_shifted  = shifted_value[FP_FRAC_W+:INT_W]; // take the integer part

  // count leading zeros

  logic [$clog2(FP_FRAC_W)-1:0] leading_zeros;

  lz_counter #(
  .WIDTH(FP_FRAC_W)
  ) lz_counter (
    .data_in(frac_shifted),
    .leading_zeros(leading_zeros)
  );

  logic out_zero;
  assign out_zero = leading_zeros == FP_FRAC_W; // all zeros in the fraction part

  // normalize float, including hidden bit

  fp_frac_t frac_norm;
  assign frac_norm = (frac_shifted << leading_zeros) << 1; // The extra 1 is the hidden 1 bit in MSB
  fp_exp_t exp_norm;
  assign exp_norm = FP_EXP_BIAS - 1 - leading_zeros;

  // output

  always_comb begin
    if (is_zero || (gte_one && out_zero)) begin
      out_frac = 64'h0; // zero
    end else if (!gte_one) begin
      out_frac = in; // (0, 1), no change
    end else begin
      out_frac = {1'b0, exp_norm, frac_norm}; // correct output
    end
  end

  always_comb begin
    if (is_zero || !gte_one) begin
      out_int = 0; // [0,1)
    end else begin
      out_int = int_shifted; // correct output
    end
  end
endmodule

module float_fractional_registered #(
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

  fp_int_frac #(
    .INT_W(INT_W)
  ) inst (
    .in(_in),
    .out_frac(_out_frac),
    .out_int(_out_int)
  );
endmodule
