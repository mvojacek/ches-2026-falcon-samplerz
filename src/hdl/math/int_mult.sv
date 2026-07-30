`timescale 1ns / 1ps

module int_mult #(
    parameter A_W = 64,
    parameter B_W = 64,
    parameter OUT_W = 64,
    parameter OUT_SHIFT = 64 // corresponds to dividing result by 2^OUT_SHIFT
)(
    input logic [A_W-1:0] a,
    input logic [B_W-1:0] b,
    output logic [OUT_W-1:0] out
);
    logic [A_W+B_W-1:0] prod;
    assign prod = a * b;
    assign out = prod[OUT_SHIFT+:OUT_W];
endmodule

module int_mult_registered #(
    parameter A_W = 64,
    parameter B_W = 64,
    parameter OUT_W = 64,
    parameter OUT_SHIFT = 64 // corresponds to dividing result by 2^OUT_SHIFT
)(
    input logic clk,
    input logic [A_W-1:0] a,
    input logic [B_W-1:0] b,
    output logic [OUT_W-1:0] out
);
    logic [A_W-1:0] a_reg;
    logic [B_W-1:0] b_reg;
    logic [OUT_W-1:0] out_wire;
    int_mult #(
        .A_W(A_W),
        .B_W(B_W),
        .OUT_W(OUT_W),
        .OUT_SHIFT(OUT_SHIFT)
    ) int_mult_inst (
        .a(a_reg),
        .b(b_reg),
        .out(out_wire)
    );

    always_ff @(posedge clk) begin
        a_reg <= a;
        b_reg <= b;
        out <= out_wire;
    end
endmodule
