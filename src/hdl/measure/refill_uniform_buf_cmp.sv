`timescale 1ns/1ps

module refill_uniform_buf_cmp (
    input  logic        clk,
    input  logic        rst,

    refill_if.sink      refill_port,

    output logic [63:0] out,
    output logic        out_valid,
    input  logic [5:0]  used_bits,
    input  logic        used
);

    refill_uniform_buf #(
        .OUT_W(64),
        .HOT_BITS(5),
        .HOT_BITS_DEPTH(2),
        .FAST_BUFS(3)
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
