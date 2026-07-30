`timescale 1ns/1ps

package samplerz_pkg;
    localparam MU_INT_W = 32;
    localparam Z_W = 5;
    localparam Z_SQ_W = Z_W*2;

    typedef enum logic {Z_POS_PLUS1=1, Z_NEG=0} z_b_t;
    typedef logic [Z_W-1:0] z_t;
    typedef logic [Z_SQ_W-1:0] z_sq_t;
    typedef struct packed {
        z_t z;
        z_b_t b;
    } z_split_t;

    typedef logic [MU_INT_W-1:0] mu_int_t;
    typedef enum logic {MU_POSITIVE=0, MU_NEGATIVE=1} mu_sign_t;    
    typedef struct packed {
        mu_int_t mu_int;
        mu_sign_t sign;
    } mu_sint_t;

    typedef enum logic {MU1_SEL=0, MU2_SEL=1} mu_sel_t;

    import fp_pkg::fp_t;

    localparam fp_t SIGMA_MAX_SQ_HALF_INV = 64'd4594603506513722306;
    localparam fp_t SIGMA_MIN_F512 = 64'd4608433670533905013;
    localparam fp_t SIGMA_MIN_F1024 = 64'd4608525754002622308;

    localparam BASE_SAMPLER_W = 72;
    localparam REFILLABLE_BASE_SAMPLER_W = BASE_SAMPLER_W + 1;
    localparam REFILLABLE_BASE_SAMPLER_W_BITS = $clog2(REFILLABLE_BASE_SAMPLER_W);
    
    localparam BEREXP_CMP_WIDTH = 64;
    localparam BEREXP_CMP_WIDTH_BITS = $clog2(BEREXP_CMP_WIDTH);
endpackage
