`timescale 1ns / 1ps

import fp_pkg::*;

module fp_sub(
    input logic clk,
    input fp_t a, b,
    output fp_t result
);
    generate
        if (FP_SUB_LATENCY != 2)
            $error("FP_SUB_LATENCY must be 2 with current implementation");
    endgenerate

    // implement using xilinx IP, latency=2
    xilinx_fp_sub2 inst ( // @suppress "Could not find declaration"
        .aclk(clk), // input wire aclk
        .s_axis_a_tvalid(1'b1), // input wire s_axis_a_tvalid
        .s_axis_a_tdata(a), // input wire [63 : 0] s_axis_a_tdata
        .s_axis_b_tvalid(1'b1), // input wire s_axis_b_tvalid
        .s_axis_b_tdata(b), // input wire [63 : 0] s_axis_b_tdata
        .m_axis_result_tvalid(), // output wire m_axis_result_tvalid
        .m_axis_result_tdata(result) // output wire [63 : 0] m_axis_result_tdata
    );

endmodule

// for timing analysis
module fp_sub_reg(
    input logic clk,
    input fp_t a, b,
    output fp_t result
);

    logic [63:0] _a, _b, _result;

    (* keep_hierarchy = "yes" *) fp_sub inst(
        .clk(clk),
        .a(_a),
        .b(_b),
        .result(_result)
    );

    always_ff @(posedge clk) begin
        _a <= a;
        _b <= b;
        result <= _result;
    end
endmodule
