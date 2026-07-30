`timescale 1ns / 1ps

import samplerz_pkg::*;

// input: z0 and sign(the b)
// output: z
// to remove the "double zero" we adjust by +1 if positive 
module adjust_z0_to_z(
    input  z_split_t in_z0, // sample to be flipped
    output z_split_t out_z // "flipped" sample
);
    assign out_z.b = in_z0.b;
    assign out_z.z = in_z0.b == Z_POS_PLUS1 ? in_z0.z + 1 : in_z0.z;
endmodule
