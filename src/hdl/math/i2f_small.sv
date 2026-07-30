`timescale 1ns/1ps

// convert a small integer and sign to a float
module i2f_small #(
    parameter INT_W = 10,

    parameter FRAC_W = 52,
    parameter EXP_W = 11,
    parameter EXP_BIAS = 11'h3FF,
    parameter FLOPOCO_FP = 0,

    localparam FLOAT_W = FRAC_W + EXP_W + 1 + (FLOPOCO_FP ? 2 : 0)
)(
    input  logic [INT_W-1:0]   in,
    input  logic               sign,
    output logic [FLOAT_W-1:0] out
);
    logic [$clog2(INT_W)-1:0] leading_zeros;
    lz_counter #(
    .WIDTH(INT_W)
    ) lz_counter_in (
        .data_in(in),
        .leading_zeros(leading_zeros)
    );

    logic [INT_W-1:0] in_shifted;
    assign in_shifted = (in << leading_zeros) << 1;

    logic [FRAC_W-1:0] mantissa;
    assign mantissa = {in_shifted, {(FRAC_W-INT_W){1'b0}}};

    logic [EXP_W-1:0] exponent;
    assign exponent = EXP_BIAS + INT_W - 1 - leading_zeros;

    generate
        if (FLOPOCO_FP) begin
            // extra bits: 00 - zero, 01 - normal, 10 - infinity, 11 - nan
            assign out = {1'b0, (in != 0), sign, exponent, mantissa};
        end else begin
            logic [FLOAT_W-1:0] out_val, out_zero;
            assign out_val = {sign, exponent, mantissa}; // allow negative zero, it won't matter
            assign out_zero = {sign, {(FLOAT_W-1){1'b0}}};
            assign out = (in == 0) ? out_zero : out_val;
        end
    endgenerate

endmodule

module i2f_small_reg #( // @suppress "File contains multiple design units"
    parameter INT_W = 5,
    parameter FRAC_W = 52,
    parameter EXP_W = 11,
    parameter EXP_BIAS = 11'h3FF,
    parameter FLOPOCO_FP = 1,

    localparam FLOAT_W = FRAC_W + EXP_W + 1 + (FLOPOCO_FP ? 2 : 0)
)(
    input  logic               clk,
    input  logic [INT_W-1:0]   in,
    input  logic               sign,
    output logic [FLOAT_W-1:0] out
);

    logic [INT_W-1:0]   _in;
    logic               _sign;
    logic [FLOAT_W-1:0] _out;

    (* keep_hierarchy = "yes" *) i2f_small #(
        .INT_W(INT_W),
        .FRAC_W(FRAC_W),
        .EXP_W(EXP_W),
        .EXP_BIAS(EXP_BIAS)
    ) i2f_small_instance (
        .in(_in),
        .sign(_sign),
        .out(_out)
    );
    always_ff @(posedge clk) begin
        _in   <= in;
        _sign <= sign;
        out   <= _out;
    end

endmodule