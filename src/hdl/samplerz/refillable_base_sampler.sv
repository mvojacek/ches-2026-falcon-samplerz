`timescale 1ns/1ps

import samplerz_pkg::*;

module refillable_base_sampler #(
    //localparam BASE_SAMPLER_W = 72,

    localparam W = BASE_SAMPLER_W + 1,
    localparam W_BITS = $clog2(W),

    // see refill_uniform_buf for details
    parameter HOT_BITS = 5+1,
    parameter HOT_BITS_DEPTH = 2,
    parameter FAST_BUFS = 2
)(
    input clk,
    input rst,

    output z_split_t sample_z0,
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

    logic [W-2:0] base_sampler_uniform_lsb;
    z_b_t flip_z_uniform;
    assign base_sampler_uniform_lsb = uniform_lsb[W-1:1];
    assign flip_z_uniform = uniform_lsb[0] ? Z_POS_PLUS1 : Z_NEG;

    logic [W_BITS-1:0] base_sampler_used_bits;
    z_t z0;
// `ifdef SZ_KEEP_HIERARCHY
//     (* keep_hierarchy = "yes" *)
// `endif
    base_sampler_pla_smart base_sampler_inst (
        .uniform(base_sampler_uniform_lsb),
        .sample(z0),
        .used(base_sampler_used_bits)
    );

    assign used_bits = base_sampler_used_bits + 1; // +1 for the flip bit

    assign sample_z0 = '{b: flip_z_uniform, z: z0};

endmodule
