`timescale 1ns/1ps

import fp_pkg::*;

// divides the input number by a fixed 2^N
module fp_div2n #(
    localparam N = 1
)(
    input fp_t in,
    output fp_t out
);
    fp_struct_t str;
    
    always_comb begin
        str = in;
        // Subtract from exponent or saturate at 0
        if (str.exp >= N) begin
            str.exp = str.exp - N;
        end else begin
            str.exp = 0;
            str.frac = 0;
        end
        out = str;
    end
endmodule
