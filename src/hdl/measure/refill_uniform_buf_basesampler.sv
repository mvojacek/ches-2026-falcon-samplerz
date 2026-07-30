`timescale 1ns/1ps

import samplerz_pkg::*;

module refill_uniform_buf_basesampler (
    input  logic        clk,
    input  logic        rst,

    refill_if.sink      refill_port,

    output logic [BASE_SAMPLER_W+1-1:0] out,
    output logic        out_valid,
    input  logic [$clog2(BASE_SAMPLER_W+1)-1:0] used_bits,
    input  logic        used
);

    refill_uniform_buf #(
        .OUT_W(BASE_SAMPLER_W+1),
        .HOT_BITS(6),
        .HOT_BITS_DEPTH(2),
        .FAST_BUFS(2)
    ) refill_uniform_buf_inst (
        .clk(clk),
        .rst(rst),
        .refill_port(refill_port),
        .out(out),
        .out_valid(out_valid),
        .used_bits(used_bits),
        .used(used)
    );

endmodule
