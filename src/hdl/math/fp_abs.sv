`timescale 1ns/1ps

import fp_pkg::*;

module fp_abs(
    input fp_t in,
    output fp_t out,
    output logic out_sign
);
    (* keep="soft" *) fp_struct_t str;
    
    always_comb begin
        str = in;
        out_sign = str.sign;
        str.sign = 0;
        out = str;
    end
endmodule
