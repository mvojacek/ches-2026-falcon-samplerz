`timescale 1ns/1ps

import samplerz_pkg::*;
import fp_pkg::*;

module samplerz_tb;

    logic clk, rst;

    fp_t mu, sigma_inv;
    mu_int_t sample_z1, sample_z2;
    logic falcon1024, start, sigma_inv_valid, sample_z1_valid, sample_z2_valid, done, full, continuous, stop, busy;
    refill_if refill_exp();
    refill_if refill_ccs();
    refill_if refill_basesampler();
    samplerz samplerz_dut (
        .clk(clk),
        .rst(rst),
        .falcon1024(falcon1024),
        .mu(mu),
        .start(start),
        .continuous(continuous),
        .stop(stop),
        .sigma_inv(sigma_inv),
        .sigma_inv_valid(sigma_inv_valid),
        .sample_z1(sample_z1),
        .sample_z2(sample_z2),
        .sample_z1_valid(sample_z1_valid),
        .sample_z2_valid(sample_z2_valid),
        .done(done),
        .refill_exp(refill_exp.sink),
        .refill_ccs(refill_ccs.sink),
        .refill_basesampler(refill_basesampler.sink),
        .full(full),
        .busy(busy)
    );

    file_refill #(.FILE("/dev/urandom")) refill_exp_inst (
        .clk(clk),
        .refill(refill_exp.source)
    );
    file_refill #(.FILE("/dev/urandom")) refill_ccs_inst (
        .clk(clk),
        .refill(refill_ccs.source)
    );
    file_refill #(.FILE("/dev/urandom")) refill_basesampler_inst (
        .clk(clk),
        .refill(refill_basesampler.source)
    );

    initial begin
        clk = 0;
        forever #1 clk = ~clk;
    end

    // relative to vivado simulation folder
    // 4 levels up is the vivado project folder
    localparam string SAMPLES_DIR = "../../../../../misc/samplerz_statistics/samples_sim";

    task run_sampling_test(
        input fp_t t_sigma_inv, t_mu1, t_mu2,
        input int cycle_count,
        input bit t_falcon1024 = 1,
        input int i
    );
        string mu1file, mu2file;
        int mu1fd, mu2fd;

        $display("Starting sigma=%e mu1=%e mu2=%e cycles=%0d at %0d num %0d", $bitstoreal(t_sigma_inv), $bitstoreal(t_mu1), $bitstoreal(t_mu2), cycle_count, $time, i);

        falcon1024 = t_falcon1024;
        continuous = 1;
        start = 0;
        sigma_inv_valid = 0;

        #1 @(negedge clk);
        // wait for full
        while (!full) @(negedge clk);

        mu = t_mu1;
        start = 1;
        @(negedge clk);

        start = 0;
        mu = t_mu2;
        @(negedge clk);

        mu = 'X;
        sigma_inv = t_sigma_inv; // the latest sginv can be inserted
        sigma_inv_valid = 1;
        @(negedge clk);

        sigma_inv_valid = 0;
        sigma_inv = 'X;

        mu1file = $sformatf("./%s/%16h_%16h.txt", SAMPLES_DIR, t_sigma_inv, t_mu1);
        mu2file = $sformatf("./%s/%16h_%16h.txt", SAMPLES_DIR, t_sigma_inv, t_mu2);
        $system($sformatf("mkdir -p ./%s", SAMPLES_DIR));
        mu1fd = $fopen(mu1file, "a");
        mu2fd = $fopen(mu2file, "a");

        for (int i = 0; i < cycle_count; i++) begin
            if (sample_z1_valid) begin
                $fdisplay(mu1fd, "%d", signed'(sample_z1));
            end
            if (sample_z2_valid) begin
                $fdisplay(mu2fd, "%d", signed'(sample_z2));
            end
            @(negedge clk);
        end
        $fclose(mu1fd);
        $fclose(mu2fd);

        $display("Finished sigma=%e mu1=%e mu2=%e cycles=%0d at %0d", $bitstoreal(t_sigma_inv), $bitstoreal(t_mu1), $bitstoreal(t_mu2), cycle_count, $time);
    endtask

    `include "data/samplerz1024_sigma_mus_dataset.sv"

    localparam int NUM_SAMPLES = 100;
    localparam int SAMPLE_SUCCESS_RATE = 57;
    localparam int NUM_SAMPLE_ATTEMPTS = NUM_SAMPLES * 100 / SAMPLE_SUCCESS_RATE;
    localparam int NUM_CYCLES = (
    samplerz_dut.SAMPLERZ_PIPELINE_DEPTH + samplerz_dut.berexp_inst.BEREXP_PIPELINE_DEPTH // pipeline fill
    + NUM_SAMPLE_ATTEMPTS * 2 // sample attempts, for each mu
    );

    localparam int INDICES[] = '{ // some random indices from the dataset
        780, 873, 297, 363, 828, 217, 164, 879, 72, 337
    };

    initial begin
        testcase_sigma_mu_t t;

        falcon1024 = 1;
        continuous = 1;
        start = 0;
        stop = 0;
        sigma_inv_valid = 0;

        rst = 1;
        #1 @(negedge clk);

        rst = 0;
        // wait for full
        while (!full) @(negedge clk);

        // run all tests
        foreach (INDICES[i]) begin
            t = testcases_sigma_mu[INDICES[i]];
            run_sampling_test(
                t.sigma_inv,
                t.mu1,
                t.mu2,
                NUM_CYCLES,
                falcon1024,
                i
            );
            #1 @(negedge clk);
        end

        $finish;
    end
endmodule
