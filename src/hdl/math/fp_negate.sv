`timescale 1ns/1ps

import fp_pkg::*;

module fp_negate(
    input fp_t in,
    output fp_t out
);
    fp_struct_t str;
    
    always_comb begin
        str = in;
        str.sign = ~str.sign;
        out = str;
    end
endmodule
