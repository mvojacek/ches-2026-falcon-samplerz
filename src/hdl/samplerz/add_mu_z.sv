`timescale 1ns / 1ps

import samplerz_pkg::*;

module add_mu_z(
    input mu_sint_t mu,
    input z_split_t z0, // the adjustment to z is done internally
    output mu_int_t result
);
    always_comb begin
        case ({mu.sign, z0.b})
            // mu here is only the *absolute value integer part* of the actual mu value
            // mu + z is regular falcon algorithm
            // however, if mu was negative, we need to flip the resulting sample
            {MU_POSITIVE, Z_NEG}:       result <=  mu.mu_int - z0.z; //  |mu| - z0     =  |mu| + (-z0)    =  mu + z
            {MU_POSITIVE, Z_POS_PLUS1}: result <=  mu.mu_int + z0.z + 1; //  |mu| + z0 + 1 =  |mu| + (z0 + 1) =  mu + z
            {MU_NEGATIVE, Z_NEG}:       result <= -mu.mu_int + z0.z; // -|mu| + z0     = -|mu| - (-z0)    = -mu - z
            {MU_NEGATIVE, Z_POS_PLUS1}: result <= -mu.mu_int - z0.z - 1; // -|mu| - z0 - 1 = -|mu| - (z0 + 1) = -mu - z
            default: result <= 'X;
        endcase
    end
endmodule
