`timescale 1ns/1ps

import fp_pkg::*;

// returns floor(2^EXP * in), preserving precision
// assumes input is in [0, 1]
module float_2exp_floor #(
  parameter EXP = 64,
  localparam INT_W = EXP+1
) (
  input  fp_t in,
  output logic [INT_W-1:0] out_int
);
  typedef logic [FP_EXP_W-1:0] exp_t;
  typedef logic [FP_FRAC_W-1:0] frac_t;
  typedef logic [INT_W-1:0] int_t;

  (* keep="soft" *) logic  sign;
  exp_t  exp;
  frac_t frac;
  assign {sign, exp, frac} = in;

  exp_t shift_amount;
  // real_exp = exp - EXP_BIAS // always negative or zero
  // we shift by the amount of -real_exp to make to normalize
  // -real_exp = EXP_BIAS - exp
  // +INT_W // make it a fraction of a fixed-point number with INT_W fractional bits
  // -EXP // apply the user multiplier
  assign shift_amount = FP_EXP_BIAS + INT_W - EXP - exp; // shift amount is always positive if input is in [0, 1)

  // prepare large enough integer to perform the shift in
  logic [INT_W:0] int_to_shift;
  generate
    if (INT_W > FP_FRAC_W) begin
      // we need padding into which to possibly shift the fraction
      logic [INT_W-FP_FRAC_W-1:0] padding;
      assign padding = 0;
      assign int_to_shift = {1'b1, frac, padding};
    end else begin
      // no padding needed, truncate the fraction so MSBs match
      assign int_to_shift = {1'b1, frac[FP_FRAC_W-1:FP_FRAC_W-INT_W]};
    end
  endgenerate

  // perform the shift
  int_t int_shifted;
  assign int_shifted = int_to_shift >> shift_amount;

  assign out_int = int_shifted;
endmodule

module float_2exp_floor_registered #(
  parameter EXP = 64
)(
  input logic clk,
  input  logic [63:0] in,
  output logic [EXP:0] out
);
  logic [63:0] in_reg;
  logic [EXP:0] out_wire;
  always_ff @(posedge clk) begin
    in_reg <= in;
    out <= out_wire;
  end

  float_2exp_floor #(
  .EXP(EXP)
  ) float_2exp_floor_inst (
    .in(in_reg),
    .out_int(out_wire)
  );
endmodule
