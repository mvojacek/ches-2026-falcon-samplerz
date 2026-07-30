`timescale 1ns / 1ps

module base_sampler_pla_smart_tb;

    localparam SIM_TIME = 1_000_000;  // Simulation time in ns = number of samples
    localparam ROUNDS = 20; // number of times to run the simulation (with separate bins)
    localparam SAMPLE_MIN = 0;
    localparam SAMPLE_MAX = 18;
    localparam USED_MIN = 1;
    localparam USED_MAX = 72;
    
    localparam IN_BITS = 72;

    logic [IN_BITS-1:0] uniform;
    logic [4:0] sample;
    logic [6:0] used;

    int sample_histogram [SAMPLE_MIN:SAMPLE_MAX];
    int used_histogram [USED_MIN:USED_MAX];

    int error_count = 0;

    base_sampler_pla_smart dut (
        .uniform(uniform),
        .sample(sample),
        .used(used)
    );
    
    function logic[7:0] random8;
        automatic logic[31:0] r = $urandom;
        return r[0+:8] ^ r[8+:8] ^ r[16+:8] ^ r[24+:8];
    endfunction

    initial begin
        $display("Starting testbench...");
        $display("sample_counts = [None] * %0d", ROUNDS);
        $display("used_counts = [None] * %0d", ROUNDS);
        for (int round = 0; round < ROUNDS; round++) begin
        $srandom(140 + round);

        foreach (sample_histogram[i]) sample_histogram[i] = 0;
        foreach (used_histogram[i]) used_histogram[i] = 0;

        for (int t = 0; t < SIM_TIME; t += 1) begin
            // extra randomness in important LSB bits for better uniformity
            uniform = {$urandom, $urandom, $urandom ^ $urandom ^ random8() ^ random8()} & {IN_BITS{1'b1}};
            #1;

            if (^sample === 1'bx || ^sample === 1'bz) begin
                $error("Unknown (X/Z) value detected on sample at time %0t: %b", $time, sample);
                error_count++;
            end else if (sample >= SAMPLE_MIN && sample <= SAMPLE_MAX) begin
                sample_histogram[sample]++;
            end else begin
                $error("Unexpected sample value: %0d at time %0t", sample, $time);
                error_count++;
            end

            if (^used === 1'bx || ^used === 1'bz) begin
                $error("Unknown (X/Z) value detected on used at time %0t: %b", $time, used);
                error_count++;
            end else if (used >= USED_MIN && used <= USED_MAX) begin
                used_histogram[used]++;
            end else begin
                $error("Unexpected used value: %0d at time %0t", used, $time);
                error_count++;
            end
        end
        
        $write("sample_counts[%0d] = [", round);
        foreach (sample_histogram[i]) begin
            $write("[%0d, %0d], ", i, sample_histogram[i]);
        end
        $display("]");
        $write("used_counts[%0d] = [", round);
        foreach (used_histogram[i]) begin
            $write("[%0d, %0d], ", i, used_histogram[i]);
        end
        $display("]");
        
        end

        $display("\nSimulation complete. Total errors: %0d", error_count);
        $finish;
    end

endmodule
