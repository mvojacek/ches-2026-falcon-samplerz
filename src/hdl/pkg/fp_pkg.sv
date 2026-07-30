`timescale 1ns/1ps

package fp_pkg;
    localparam int unsigned FP_MUL_LATENCY = 2;
    localparam int unsigned FP_ADD_LATENCY = 2;
    localparam int unsigned FP_SUB_LATENCY = 2;
    localparam int unsigned FP_EXP_LATENCY = 9;

    localparam int unsigned FP_W = 64;
    localparam int unsigned FP_EXP_W = 11;
    localparam int unsigned FP_FRAC_W = 52;
    
    typedef logic [FP_W-1:0] fp_t;
    typedef logic [FP_EXP_W-1:0] fp_exp_t;
    typedef logic [FP_FRAC_W-1:0] fp_frac_t;
    typedef enum logic {FP_POSITIVE=0, FP_NEGATIVE=1} fp_sign_t;

    localparam fp_exp_t FP_EXP_BIAS = 11'h3FF;

    typedef struct packed {
        logic sign;
        fp_exp_t exp;
        fp_frac_t frac;
    } fp_struct_t;

    localparam int unsigned FLOPO_W = FP_W + 2;
    typedef logic [FLOPO_W-1:0] flopo_t;
    typedef enum bit[1:0] {
        EX_ZERO = 2'b00,
        EX_NORMAL = 2'b01,
        EX_INFINITY = 2'b10,
        EX_NAN = 2'b11
    } flopo_ex_t;

    typedef struct packed {
        flopo_ex_t ex;
        logic sign;
        fp_exp_t exp;
        fp_frac_t frac;
    } flopo_struct_t;
endpackage
