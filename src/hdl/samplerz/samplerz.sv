`timescale 1ns/1ps

import fp_pkg::*;
import samplerz_pkg::*;

// Pipelined samplerz module for the falcon signature scheme.
// The mu port accepts mu1 on the same cycle as start=1, and mu2 on the next cycle. The mu values are stored internally.
// The sigma_inv is part of the private key and needs to enter the module through its dedicated port at the latest on the cycle following mu2 load.
// It takes 19 cycles for the pipeline to fill, from the nineteenth cycle onward there is a chance the output sample will become valid.
// Once both samples are valid, the done signal will be set to 1, on average after 22.12 cycles, because the outputs are registered.
// In continuous mode, the output samples and valid signals are updated indefinitely.
module samplerz #(
)(
    input logic clk, rst,

    input logic falcon1024,

    input fp_t mu,
    input logic start, continuous, stop,

    input fp_t sigma_inv,
    input logic sigma_inv_valid,

    output mu_int_t sample_z1, sample_z2,
    output logic sample_z1_valid, sample_z2_valid,
    output logic done, busy,

    refill_if.sink refill_exp,
    refill_if.sink refill_ccs,
    refill_if.sink refill_basesampler,

    output logic full
);

    // SAMPLERZ:
    // | A | Aout | B | C | D | BerExp // (z-r)^2 path
    // | 2 |    1 | 2 | 2 | 2 |
    // |       G      | E | D | BerExp // z0^2 path
    // |       5      | 2 | 2 |
    // |       G      |   J   | BerExp // z0 path into berexp
    // |       5      |   4   |

    localparam SAMPLERZ_PIPELINE_DEPTH
    = FP_SUB_LATENCY // A
    + 1 // A out
    + FP_MUL_LATENCY // B
    + FP_MUL_LATENCY // C/E
    + FP_SUB_LATENCY; // D

    localparam AB_PIPELINE_DEPTH
    = FP_SUB_LATENCY // A
    + 1 // A out
    + FP_MUL_LATENCY; // B

    localparam CD_PIPELINE_DEPTH
    = FP_MUL_LATENCY // C/E
    + FP_SUB_LATENCY; // D

    // ================
    // States
    // ================

    // ==== SGINV ====

    typedef enum logic [1:0] {
        SGINV_IDLE='b00, // waiting for inverted sigma
        SGINV_MUL1='b01, // waiting for multiplication
        SGINV_MULDONE='b10 // mul done, save to registers: ccs and sigma_sq_half_inv
    } state_sginv_t;
    state_sginv_t state_sginv, state_sginv_next;

    logic fp_mul_B_use_siginv; // use sigma_inv for multiplication in B (squarer)
    logic fp_mul_E_use_siginv; // use sigma_inv for multiplication in E (sg_inv*sigma_min)
    logic fp_mul_E_use_sigma_min; // use sigma_min for multiplication in E (sg_inv*sigma_min)
    logic sigma_sq_half_inv_we; // save calculation result
    logic berexp_new_ccs; // direct berexp to accept new ccs

    always_comb begin
        fp_mul_B_use_siginv = 0;
        fp_mul_E_use_siginv = 0;
        fp_mul_E_use_sigma_min = 0;
        sigma_sq_half_inv_we = 0;
        berexp_new_ccs = 0;

        state_sginv_next = state_sginv;

        if (stop) begin
            state_sginv_next = SGINV_IDLE;
        end else if (sigma_inv_valid) begin // in any state, if sigma_inv is valid, we should take it
            state_sginv_next = SGINV_MUL1;
            fp_mul_B_use_siginv = 1; // input sigma_inv into squarer B
            fp_mul_E_use_siginv = 1; // calculate ccs in E
            fp_mul_E_use_sigma_min = 1; // calculate ccs in E
        end else begin
            // FSM
            case (state_sginv)
                SGINV_IDLE: begin
                    // waiting for sigma_inv_valid (logic below)
                    state_sginv_next = SGINV_IDLE;
                end
                SGINV_MUL1: begin
                    // waiting for multiplications to finish
                    state_sginv_next = SGINV_MULDONE;
                end
                SGINV_MULDONE: begin
                    state_sginv_next = SGINV_IDLE;
                    // multiplications are done - save ccs and sigma_sq_half_inv
                    sigma_sq_half_inv_we = 1; // write sigma_sq_half_inv
                    berexp_new_ccs = 1; // direct berexp to accept new ccs
                end
                default: begin
                    state_sginv_next = SGINV_IDLE;
                end
            endcase
        end
    end

    always_ff @(posedge clk) begin
        if (rst) begin
            state_sginv <= SGINV_IDLE;
        end else begin
            state_sginv <= state_sginv_next;
        end
    end

    // ==== MU ====

    typedef enum logic [1:0] {
        IDLE='b00,
        INIT_MU2='b01, // mul2 is arriving
        MU1='b10, // process next sample with saved MU1
        MU2='b11 // process next sample with saved MU2
    } state_mu_t;
    state_mu_t state_mu, state_mu_next;

    mu_sel_t sel_mu2_A; // select which mu to use for A inputs (start of pipeline)
    mu_sel_t sel_mu2_berexp; // select which mu to use at berexp inputs

    logic use_r_direct; // use r directly from mu_r
    logic use_r_mu2; // use stored mu2's r as the r
    logic r1_we, r2_we; // write to r1 and r2 registers
    logic s1_we, s2_we; // write to s1 and s2 registers
    logic z0_used; // z0 is used and needs to be generated (all the time except when idle)

    always_comb begin
        sel_mu2_A = (state_mu == INIT_MU2 || state_mu == MU2) ? MU2_SEL : MU1_SEL;
        sel_mu2_berexp = mu_sel_t'((sel_mu2_A + SAMPLERZ_PIPELINE_DEPTH) & 1); // get selector parity after pipeline depth
        use_r_mu2 = sel_mu2_A;

        use_r_direct = 0;
        r1_we = 0;
        r2_we = 0;
        s1_we = 0;
        s2_we = 0;
        z0_used = 0;

        state_mu_next = state_mu;
        if (stop) begin
            state_mu_next = IDLE;
        end else if (start) begin
            state_mu_next = INIT_MU2;
            // we are receiving mu1 - save it, and also calculate with it directly
            use_r_direct = 1; // use mu/r directly in A
            r1_we = 1; // write to r1
            s1_we = 1; // write to s1
            z0_used = 1;
        end else begin
            case (state_mu)
                IDLE: begin
                    // waiting for mu1
                    state_mu_next = IDLE;
                end
                INIT_MU2: begin
                    state_mu_next = MU1;
                    // we are receiving mu2 - save it, and also calculate with it directly
                    use_r_direct = 1; // use mu/r directly in A
                    r2_we = 1; // write to r2
                    s2_we = 1; // write to s2
                    z0_used = 1;
                end
                MU1: begin
                    state_mu_next = MU2;
                    z0_used = !sample_z1_valid || continuous; // z0 is used only if the sample is not valid
                    if (done && !continuous)
                        state_mu_next = IDLE;
                end
                MU2: begin
                    state_mu_next = MU1;
                    z0_used = !sample_z2_valid || continuous; // z0 is used only if the sample is not valid
                    if (done && !continuous)
                        state_mu_next = IDLE;
                end
                default: begin
                    state_mu_next = IDLE;
                end
            endcase
        end
    end

    always_ff @(posedge clk) begin
        if (rst) begin
            state_mu <= IDLE;
        end else begin
            state_mu <= state_mu_next;
        end
    end

    assign busy = state_mu != IDLE || state_sginv != SGINV_IDLE || start || sigma_inv_valid;

    // ================
    // Input acceptance
    // ================

    // absolute value and sign decomposition
    fp_t mu_abs;
    logic mu_abs_sign;
    mu_sign_t mu_sign;
    assign mu_sign = mu_abs_sign == 0 ? MU_POSITIVE : MU_NEGATIVE;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    fp_abs fp_mu_abs (
        .in(mu),
        .out(mu_abs),
        .out_sign(mu_abs_sign)
    );

    // interger and fraction decomposition
    mu_int_t mu_s;
    fp_t mu_r;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    fp_int_frac #(
    .INT_W(MU_INT_W)
    ) fp_int_frac_instance (
        .in(mu_abs),
        .out_frac(mu_r),
        .out_int(mu_s)
    );

    mu_sint_t s1, s2;
    fp_t r1, r2;
    always_ff @(posedge clk) begin
        if (rst) begin
            {s1, r1, s2, r2} <= '0;
        end else begin
            if (s1_we) begin
                s1.sign <= mu_sign;
                s1.mu_int <= mu_s;
            end
            if (s2_we) begin
                s2.sign <= mu_sign;
                s2.mu_int <= mu_s;
            end
            if (r1_we) begin
                r1 <= mu_r;
            end
            if (r2_we) begin
                r2 <= mu_r;
            end
        end
    end

    fp_t selected_mu_r;
    always_comb begin
        if (use_r_direct) begin
            selected_mu_r = mu_r;
        end else if (use_r_mu2) begin
            selected_mu_r = r2;
        end else begin
            selected_mu_r = r1;
        end
    end

    // ================
    // BaseSampler
    // ================

    z_split_t basesampler_z0, z0, z0_next;
    logic basesampler_z0_valid, z0_valid, z0_valid_next;
    logic basesampler_z0_used;

`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    refillable_base_sampler #(
        .HOT_BITS(6),
        .HOT_BITS_DEPTH(2),
        .FAST_BUFS(2)
    ) base_sampler (
        .clk(clk),
        .rst(rst),
        .sample_z0(basesampler_z0),
        .valid(basesampler_z0_valid),
        .used(basesampler_z0_used),
        .refill_port(refill_basesampler)
    );

    always_comb begin
        z0_valid_next = z0_valid;
        z0_next = z0;

        basesampler_z0_used = 0;
        if (rst) begin
            z0_next = '0;
            z0_valid_next = 0;
        end else begin
            if (z0_used && z0_valid_next) begin
                z0_valid_next = 0; // it was used by the pipeline
            end

            if (!z0_valid_next && basesampler_z0_valid) begin
                z0_next = basesampler_z0; // get new sample
                z0_valid_next = 1;
                basesampler_z0_used = 1; // we consumed it from the base sampler
            end
        end
    end

    always_ff @(posedge clk) begin
        z0 <= z0_next;
        z0_valid <= z0_valid_next;
    end

    // sample valid chain
    logic[SAMPLERZ_PIPELINE_DEPTH-1:0] sample_valid_chain;
    always_ff @(posedge clk) begin
        if (rst) begin
            sample_valid_chain <= '0;
        end else if (start) begin
            sample_valid_chain <= {{SAMPLERZ_PIPELINE_DEPTH-1{1'b0}}, z0_valid && z0_used};
        end else begin
            sample_valid_chain <= {sample_valid_chain[SAMPLERZ_PIPELINE_DEPTH-2:0], z0_valid && z0_used};
        end
    end
    logic sample_valid_berexp;
    assign sample_valid_berexp = sample_valid_chain[SAMPLERZ_PIPELINE_DEPTH-1];

    // ================
    // Path A-B-C
    // ================

    // z0 to z conversion, 0 cycles
    z_split_t z;
    adjust_z0_to_z z0_to_z_inst (
        .in_z0(z0),
        .out_z(z)
    );

    // convert to float, 0 cycles
    fp_t z_fp;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    i2f_small #(
        .INT_W(Z_W),
        .FRAC_W(FP_FRAC_W),
        .EXP_W(FP_EXP_W),
        .EXP_BIAS(FP_EXP_BIAS),
        .FLOPOCO_FP(0)
    ) i2f_small_instance (
        .in(z.z),
        .sign(z.b == Z_POS_PLUS1 ? 1'b0 : 1'b1),
        .out(z_fp)
    );

    // A: sub: z_fp - r (3 cycles)
    fp_t fp_sub_A_result_inreg, fp_sub_A_result;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    fp_sub fp_sub_A (
        .clk(clk),
        .a(z_fp),
        .b(selected_mu_r),
        .result(fp_sub_A_result_inreg)
    );
    // extra pipeline stage - fp sub has no inner output stage
    always_ff @(posedge clk) fp_sub_A_result <= fp_sub_A_result_inreg;

    // B: square: (z_fp - r)^2 OR sg_inv^2 (2 cycles)
    fp_t fp_mul_B_result, fp_mul_B_input;
    assign fp_mul_B_input = fp_mul_B_use_siginv ? sigma_inv : fp_sub_A_result;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    fp_mul fp_mul_B (
        .clk(clk),
        .a(fp_mul_B_input),
        .b(fp_mul_B_input),
        .result(fp_mul_B_result)
    );

    // sigma_sq_half_inv register
    fp_t sigma_sq_half_inv, sigma_sq_half_inv_inreg;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    fp_div2n fp_div2n_inst (
        .in(fp_mul_B_result),
        .out(sigma_sq_half_inv_inreg)
    );
    always_ff @(posedge clk) begin
        if (sigma_sq_half_inv_we) begin
            sigma_sq_half_inv <= sigma_sq_half_inv_inreg;
        end
    end

    // C: mul: (z_fp - r)^2 * sigma_sq_half_inv (2 cycles)
    fp_t fp_mul_C_result;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    fp_mul fp_mul_C (
        .clk(clk),
        .a(fp_mul_B_result),
        .b(sigma_sq_half_inv),
        .result(fp_mul_C_result)
    );

    // ================
    // Path G-E-D and G-J
    // ================

    // G: delay compensation for A-B
    z_split_t z0_after_G;
    delay #(
        .delay_t(z_split_t),
        .STAGES(AB_PIPELINE_DEPTH)
    ) delay_z0_G (
        .clk(clk),
        .in(z0),
        .out(z0_after_G)
    );

    // square z0 and convert to float, 0 cycles
    logic [Z_SQ_W-1:0] z0_sq;
    assign z0_sq = z0_after_G.z * z0_after_G.z;
    fp_t z0_sq_fp;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    i2f_small #(
        .INT_W(Z_SQ_W),
        .FRAC_W(FP_FRAC_W),
        .EXP_W(FP_EXP_W),
        .EXP_BIAS(FP_EXP_BIAS),
        .FLOPOCO_FP(0)
    ) i2f_small_z0_sq (
        .in(z0_sq),
        .sign(1'b0),
        .out(z0_sq_fp)
    );

    // E: mul: z0^2 * sigma_max_sq_half_inv (2 cycles)
    // OR: sigma_inv * sigma_min
    fp_t fp_mul_E_result, fp_mul_E_input_var, fp_mul_E_input_const, sigma_min;
    assign sigma_min = falcon1024 ? SIGMA_MIN_F1024 : SIGMA_MIN_F512;
    assign fp_mul_E_input_var = fp_mul_E_use_siginv ? sigma_inv : z0_sq_fp;
    assign fp_mul_E_input_const = fp_mul_E_use_sigma_min ? sigma_min : SIGMA_MAX_SQ_HALF_INV;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    fp_mul fp_mul_E (
        .clk(clk),
        .a(fp_mul_E_input_var),
        .b(fp_mul_E_input_const),
        .result(fp_mul_E_result)
    );

    // D: sub: E - C = (z0^2 * sigma_max_sq_half_inv) - ((z-r)^2 * sigma_sq_half_inv) = -x (2 cycles)
    // note that we directly calculate -x and not x!
    fp_t fp_sub_D_result;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    fp_sub fp_sub_D (
        .clk(clk),
        .a(fp_mul_E_result),
        .b(fp_mul_C_result),
        .result(fp_sub_D_result)
    );

    // J: delay compensation for E-D
    z_split_t z0_after_J;
    delay #(
        .delay_t(z_split_t),
        .STAGES(CD_PIPELINE_DEPTH)
    ) delay_instance_J (
        .clk(clk),
        .in(z0_after_G),
        .out(z0_after_J)
    );

    // =================
    // BerExp
    // =================

    fp_t berexp_neg_x, berexp_ccs;
    z_split_t berexp_z0;
    assign berexp_neg_x = fp_sub_D_result;
    assign berexp_ccs = fp_mul_E_result;
    assign berexp_z0 = z0_after_J;

`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    berexp #(
    .INPUT_IS_MINUS_X(1)
    ) berexp_inst (
        .clk(clk),
        .rst(rst),

        .start(start),
        .continuous(continuous),

        .x(berexp_neg_x),
        .mu_sel_x(sel_mu2_berexp),
        .x_valid(sample_valid_berexp),

        .ccs(berexp_ccs),
        .new_ccs(berexp_new_ccs),

        .z0(berexp_z0),

        .refill_exp(refill_exp),
        .refill_ccs(refill_ccs),

        .mu1(s1),
        .mu2(s2),

        .sample_z1(sample_z1),
        .sample_z2(sample_z2),
        .sample_z1_valid(sample_z1_valid),
        .sample_z2_valid(sample_z2_valid),
        .done(done)
    );

    assign full = refill_exp.full && refill_ccs.full && refill_basesampler.full;

endmodule
