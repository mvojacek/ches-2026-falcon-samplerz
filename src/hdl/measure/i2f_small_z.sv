`timescale 1ns/1ps

import fp_pkg::*;
import samplerz_pkg::*;

module i2f_small_z (
    input  logic [Z_W-1:0] in,
    input  logic           sign,
    output fp_t            out
);

    i2f_small #(
        .INT_W(Z_W),
        .FRAC_W(FP_FRAC_W),
        .EXP_W(FP_EXP_W),
        .EXP_BIAS(FP_EXP_BIAS),
        .FLOPOCO_FP(0)
    ) i2f_small_inst (
        .in(in),
        .sign(sign),
        .out(out)
    );

endmodule
