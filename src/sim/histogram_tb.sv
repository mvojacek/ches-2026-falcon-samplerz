`timescale 1ns/1ps

module histogram_tb;

    parameter BINS = 40;
    parameter BIN_W = 32;
    parameter BINS_BITS = $clog2(BINS);

    logic clk, rst;
    logic [BIN_W-1:0] sample;
    logic sample_valid;
    logic bounds_error;
    logic [BIN_W-1:0] hist [BINS-1:0];
    logic [BIN_W-1:0] hist_pivot_value;
    logic [BINS_BITS-1:0] hist_pivot_index;

    histogram #(
        .BINS(BINS),
        .BIN_W(BIN_W)
    ) dut (
        .clk(clk),
        .rst(rst),
        .sample(sample),
        .sample_valid(sample_valid),
        .bounds_error(bounds_error),
        .hist(hist),
        .hist_pivot_value(hist_pivot_value),
        .hist_pivot_index(hist_pivot_index)
    );

    initial begin
        clk = 0;
        forever #1 clk = ~clk;
    end

    int unsigned range_start, range_end;
    int unsigned theoretical_hist [BINS-1:0];
    int unsigned random_sample;

    initial begin
        clk = 0;
        rst = 0;
        sample = 0;
        sample_valid = 0;
        for (int i = 0; i < BINS; i++) theoretical_hist[i] = 0;

        @(negedge clk);
        rst = 1;
        @(negedge clk);
        rst = 0;

        range_start = $urandom_range(0, 100);
        range_end = range_start + (BINS / 2 - 1);

        for (int i = 0; i < 200; i++) begin
            random_sample = $urandom_range(range_start, range_end);
            sample = random_sample;
            sample_valid = 1;
            @(negedge clk);
            sample_valid = 0;
            @(negedge clk);

            if (i == 0) begin
                theoretical_hist[BINS/2] += 1;
            end else if (random_sample >= range_start && random_sample <= range_end) begin
                int offset = random_sample - hist_pivot_value;
                theoretical_hist[BINS/2 + offset] += 1;
            end
        end

        for (int i = 0; i < BINS; i++) begin
            if (theoretical_hist[i] !== hist[i]) begin
                $error("Mismatch at bin %0d: Expected %0d, Got %0d", i, theoretical_hist[i], hist[i]);
            end
        end
        $display("Histograms match!");

        // Test for out-of-bounds error
        if (bounds_error) $error("bounds_error should be 0 before starting out-of-bounds tests");

        @(negedge clk);
        sample = hist_pivot_value - (BINS / 2); // Just below the valid range
        sample_valid = 1;
        @(negedge clk);
        sample_valid = 0;
        @(negedge clk);
        if (!bounds_error) $error("Expected bounds_error for sample just below valid range");

        $display("Done!");
        $finish;
    end

endmodule
