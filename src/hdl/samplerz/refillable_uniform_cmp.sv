`timescale 1ns/1ps

module refillable_uniform_cmp #(
    parameter W = 64,
    localparam W_BITS = $clog2(W),

    // see refill_uniform_buf for details
    parameter HOT_BITS = 5,
    parameter HOT_BITS_DEPTH = 2,
    parameter FAST_BUFS = 3
)(
    input clk,
    input rst,

    input logic [W:0] in, // in is one bit larger than W to allow 100% chance of success
    output logic in_gt, in_lt, eq,
    output logic valid,
    input logic used, // can be used to prevent randomness consumption

    refill_if.sink refill_port
);

    logic [W-1:0] uniform_lsb;
    logic [W_BITS-1:0] used_bits;
// `ifdef SZ_KEEP_HIERARCHY
//     (* keep_hierarchy = "yes" *)
// `endif
    refill_uniform_buf #(
        .OUT_W(W),
        .HOT_BITS(HOT_BITS),
        .HOT_BITS_DEPTH(HOT_BITS_DEPTH),
        .FAST_BUFS(FAST_BUFS)
    ) refill_uniform_buf_instance (
        .clk(clk),
        .rst(rst),
        .refill_port(refill_port),
        .out(uniform_lsb),
        .out_valid(valid),
        .used_bits(used_bits),
        .used(used)
    );

    logic [W-1:0] uniform_msb;
    assign uniform_msb = {<<{uniform_lsb}};
// `ifdef SZ_KEEP_HIERARCHY
//     (* keep_hierarchy = "yes" *)
// `endif
    lazy_uniform_cmp #(
    .W(W)
    ) cmp (
        .in(in),
        .uniform(uniform_msb),
        .in_gt(in_gt), .in_lt(in_lt), .eq(eq),
        .used_bits(used_bits)
    );

endmodule
