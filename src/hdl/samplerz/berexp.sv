`timescale 1ns/1ps

import fp_pkg::*;
import samplerz_pkg::*;

module berexp #(
    parameter INPUT_IS_MINUS_X = 0
)(
    input logic clk, rst,

    input logic start, // signals from samplerz that new mu values are loaded - discard all samples
    input logic continuous, // continuous mode - keep updating output registers as long as samples are valid

    input fp_t x,
    input mu_sel_t mu_sel_x, // the mu sel to which x belongs
    input logic x_valid,

    input fp_t ccs,
    input logic new_ccs,

    input z_split_t z0, // the adjustment to z is done in add_mu_z

    refill_if.sink refill_exp,
    refill_if.sink refill_ccs,

    input mu_sint_t mu1, mu2,

    output mu_int_t sample_z1, sample_z2,
    output logic sample_z1_valid, sample_z2_valid,
    output logic done
);

    localparam CMP_WIDTH = BEREXP_CMP_WIDTH;

    localparam BEREXP_PIPELINE_DEPTH = FP_EXP_LATENCY;

    // ===============
    // EXP + CMP path
    // ===============

    fp_t neg_x;
    generate
        if (INPUT_IS_MINUS_X) begin
            // already have -x, do nothing
            assign neg_x = x;
        end else begin
            // -x
            fp_negate i_neg_x (
                .in(x),
                .out(neg_x)
            );
        end
    endgenerate

    // e^-x
    fp_t exp_x;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    fp_exp i_exp_x (
        .clk(clk),
        .a(neg_x),
        .result(exp_x)
    );

    // e^-x or ccs
    fp_t exp_x_or_ccs;
    assign exp_x_or_ccs = new_ccs ? ccs : exp_x;

    // floor(2^64 * exp_x_or_ccs)
    logic [CMP_WIDTH:0] exp_x_or_ccs_int;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    float_2exp_floor #(
    .EXP(CMP_WIDTH)
    ) i_2exp_floor (
        .in(exp_x_or_ccs),
        .out_int(exp_x_or_ccs_int)
    );

    // ccs register
    logic [CMP_WIDTH:0] ccs_reg;
    always_ff @(posedge clk) begin
        if (rst) begin
            ccs_reg <= '0;
        end else if (new_ccs) begin
            ccs_reg <= exp_x_or_ccs_int;
        end
    end

    // comparator for exp_x
    logic exp_x_success;
    logic exp_x_success_valid;
    logic exp_x_success_used;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    refillable_uniform_cmp #(
        .W(CMP_WIDTH),
        .HOT_BITS(5),
        .HOT_BITS_DEPTH(1),
        .FAST_BUFS(1)
    ) cmp_exp_x (
        .clk(clk),
        .rst(rst),
        .in(exp_x_or_ccs_int),
        .in_gt(exp_x_success),
        .in_lt(),
        .eq(),
        .valid(exp_x_success_valid),
        .used(exp_x_success_used),
        .refill_port(refill_exp)
    );

    // comparator for ccs
    logic ccs_success;
    logic ccs_success_valid;
    logic ccs_success_used;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    refillable_uniform_cmp #(
        .W(CMP_WIDTH),
        .HOT_BITS(5),
        .HOT_BITS_DEPTH(1),
        .FAST_BUFS(1)
    ) cmp_ccs (
        .clk(clk),
        .rst(rst),
        .in(ccs_reg),
        .in_gt(ccs_success),
        .in_lt(),
        .eq(),
        .valid(ccs_success_valid),
        .used(ccs_success_used),
        .refill_port(refill_ccs)
    );

    // delay x_valid by the same amount of stages as exp_x takes
    logic[BEREXP_PIPELINE_DEPTH-1:0] x_valid_chain;
    always_ff @(posedge clk) begin
        if (rst) begin
            x_valid_chain <= '0;
        end else if (start) begin
            x_valid_chain <= {{BEREXP_PIPELINE_DEPTH-1{1'b0}}, x_valid};
        end else begin
            x_valid_chain <= {x_valid_chain[BEREXP_PIPELINE_DEPTH-2:0], x_valid};
        end
    end
    // pre1 is one cycles ahead - we want to take the ccs bit early
    logic x_valid_delayed_pre1;
    (* keep="soft" *) logic x_valid_delayed; // currently not needed
    assign x_valid_delayed_pre1 = x_valid_chain[BEREXP_PIPELINE_DEPTH-2];
    assign x_valid_delayed = x_valid_chain[BEREXP_PIPELINE_DEPTH-1];

    // ccs success register
    logic ccs_success_reg;
    always_ff @(posedge clk) begin
        if (rst || start) begin
            ccs_success_reg <= 1'b0;
        end else begin
            // if ccs sampling was invalid, reject the sample
            // or if x_valid is 0, means failure earlier in the pipeline, reject
            ccs_success_reg <= ccs_success && ccs_success_valid && x_valid_delayed_pre1;
        end
    end

    // prevent random consumption in exp_x path if ccs path failed
    assign exp_x_success_used = ccs_success_reg && exp_x_success_valid; //FIXME
    // prevent random consumption in ccs path if filling
    assign ccs_success_used = x_valid_delayed_pre1 && ccs_success_valid;

    // success
    logic success;
    // if exp_x sampling is invalid, reject the sample
    assign success = ccs_success_reg && exp_x_success && exp_x_success_valid;

    // ===========
    // z sample path
    // ===========

    // delay z0 sample by the same amount of stages as exp_x takes
    z_split_t z0_delayed;
    delay #(
        .delay_t(z_split_t),
        .STAGES(FP_EXP_LATENCY)
    ) z_delay (
        .clk(clk),
        .in(z0),
        .out(z0_delayed)
    );

    // also delay mu_sel by this amount of cycles (by adding and taking parity)
    mu_sel_t mu_sel_delayed;
    assign mu_sel_delayed = mu_sel_t'((int'(mu_sel_x) + FP_EXP_LATENCY) & 1'b1);

    // select mu
    mu_sint_t mu;
    assign mu = mu_sel_delayed == MU1_SEL ? mu1 : mu2;

    // add mu+z
    mu_int_t mu_plus_z;
`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    add_mu_z mu_z_adder (
        .mu(mu),
        .z0(z0_delayed),
        .result(mu_plus_z)
    );

    // =============
    // output registers
    // =============
    
    logic sample_z1_save, sample_z2_save;
    
    always_comb begin
        sample_z1_save = mu_sel_delayed == MU1_SEL && success;
        sample_z2_save = mu_sel_delayed == MU2_SEL && success;
    end

    always_ff @(posedge clk) begin
        if (rst || start) begin
            sample_z1_valid <= 0;
            sample_z2_valid <= 0;
        end else begin
            if (continuous) begin
                sample_z1_valid <= sample_z1_save;
                sample_z2_valid <= sample_z2_save;
                sample_z1 <= sample_z1_save ? mu_plus_z : 'X;
                sample_z2 <= sample_z2_save ? mu_plus_z : 'X;
            end else begin
                if (sample_z1_save && !sample_z1_valid) begin
                    sample_z1 <= mu_plus_z;
                    sample_z1_valid <= 1;
                end
                if (sample_z2_save && !sample_z2_valid) begin
                    sample_z2 <= mu_plus_z;
                    sample_z2_valid <= 1;
                end
            end
        end
    end

    assign done = sample_z1_valid && sample_z2_valid;
endmodule
