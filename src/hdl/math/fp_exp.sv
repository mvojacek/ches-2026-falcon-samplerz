`timescale 1ns / 1ps

import fp_pkg::*;

module fp_exp(
    input logic clk,
    input fp_t a,
    output fp_t result
);
    generate
        if (FP_EXP_LATENCY != 9)
            $error("FP_EXP_LATENCY must be 9 with current implementation");
    endgenerate
    
    // implement using flopoco operator, latency=7
    fp_t x, r;
    flopoco_ieee_exp inst (
        .clk(clk),
        .x(x),
        .r(r)
    );

    // flopoco exp has long input and output paths, add register stages
    always_ff @(posedge clk) begin
        x <= a;
        result <= r;
    end

endmodule
