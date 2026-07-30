`timescale 1ns/1ps

import axi_vip_pkg::*;
import design_axi_test_axi_vip_0_0_pkg::*;

import samplerz_axi_map_pkg::*;
import fp_pkg::*;

module samplerz_axi_tb;

    logic clk, rst;

    initial begin
        clk = 0;
        forever #1 clk = ~clk;
    end

    design_axi_test_wrapper design_inst(.aclk(clk), .aresetn(~rst));

    typedef logic [31:0] word_t;
    typedef logic [63:0] double_t;

    design_axi_test_axi_vip_0_0_mst_t agent;

    localparam int AXI_ADDR_BASE = 0;

    task axi_read(input int unsigned addr, output word_t data);
        automatic xil_axi_resp_t resp;
        agent.AXI4LITE_READ_BURST(AXI_ADDR_BASE + addr, 0, data, resp);
        if (resp != XIL_AXI_RESP_OKAY) begin
            $fatal(1, "AXI_READ failed: addr=%h, status=%b", addr, resp);
        end
    endtask

    task axi_read_mask(input int unsigned addr, output word_t data, input word_t mask);
        axi_read(addr, data);
        data = data & mask;
    endtask

    task axi_read_bit(input int unsigned addr, output bit data, input int unsigned bit_pos);
        word_t read;
        axi_read(addr, read);
        data = read[bit_pos];
    endtask

    task axi_write(input int unsigned addr, input word_t data);
        automatic xil_axi_resp_t resp;
        agent.AXI4LITE_WRITE_BURST(AXI_ADDR_BASE + addr, 0, data, resp);
        if (resp != XIL_AXI_RESP_OKAY) begin
            $fatal(1, "AXI_WRITE failed: addr=%h, status=%b", addr, resp);
        end
    endtask

    task axi_write2(input int unsigned addr, input double_t data);
        axi_write(addr, data[31:0]);
        axi_write(addr + 4, data[63:32]);
    endtask

    task axi_read2(input int unsigned addr, output double_t data);
        word_t low, high;
        axi_read(addr, low);
        axi_read(addr + 4, high);
        data = {high, low};
    endtask

    // read modify write using mask
    task axi_rmw_mask(input int unsigned addr, input word_t data, input word_t mask);
        automatic word_t read;
        axi_read(addr, read);
        read = (read & ~mask) | (data & mask);
        axi_write(addr, read);
    endtask

    function word_t mask_if(input bit condition, input word_t mask);
        return condition ? mask : '0;
    endfunction

    task samplerz_check_marker();
        automatic word_t data, marker = 32'h6663737a;
        axi_read(SAMPLERZ_AXI__MARKER__DATA__ADDR, data);
        if (data != marker) begin
            $fatal(1, "Marker check failed: %h != %h", data, marker);
        end
    endtask

    task samplerz_configure(input bit falcon1024, continuous);
        axi_rmw_mask(
            SAMPLERZ_AXI__CONTROL__ADDR,
            mask_if(falcon1024, SAMPLERZ_AXI__CONTROL__FALCON1024__MASK) | mask_if(continuous, SAMPLERZ_AXI__CONTROL__CONTINUOUS__MASK),
            SAMPLERZ_AXI__CONTROL__FALCON1024__MASK | SAMPLERZ_AXI__CONTROL__CONTINUOUS__MASK
        );
    endtask

    task samplerz_params(input fp_t sigma_inv, mu1, mu2);
        $display(1, "Setting sigma_inv = %f, mu1 = %f, mu2 = %f", $bitstoreal(sigma_inv), $bitstoreal(mu1), $bitstoreal(mu2));
        axi_write2(SAMPLERZ_AXI__SGINV__ADDR, sigma_inv);
        axi_write2(SAMPLERZ_AXI__MU1__ADDR, mu1);
        axi_write2(SAMPLERZ_AXI__MU2__ADDR, mu2);
    endtask

    localparam word_t PRNG_SEED[SAMPLERZ_AXI__PRNG__SEED__ARRLEN] = {
    32'h05D44CB0,
    32'h14645D64,
    32'h3CAD6A2B,
    32'h6C9B7402,
    32'h7BEE0333,
    32'h14A429CC,
    32'h38430751,
    32'h12076FCF,
    32'h2E26385F,
    32'h18775852,
    32'h15C76338
    };

    task samplerz_init_prng();
        for (int i = 0; i < SAMPLERZ_AXI__PRNG__SEED__ARRLEN; i++) begin
            axi_write(SAMPLERZ_AXI__PRNG__SEED__ADDR + i * SAMPLERZ_AXI__PRNG__SEED__STRIDE, PRNG_SEED[i]);
        end
        axi_write2(SAMPLERZ_AXI__PRNG__COUNTER__ADDR, '0);
    endtask

    task samplerz_reset();
        axi_rmw_mask(SAMPLERZ_AXI__CONTROL__ADDR, SAMPLERZ_AXI__CONTROL__RESET__MASK, SAMPLERZ_AXI__CONTROL__RESET__MASK);
    endtask

    task samplerz_start();
        axi_rmw_mask(SAMPLERZ_AXI__CONTROL__ADDR, SAMPLERZ_AXI__CONTROL__START__MASK, SAMPLERZ_AXI__CONTROL__START__MASK);
    endtask

    task samplerz_stop();
        axi_rmw_mask(SAMPLERZ_AXI__CONTROL__ADDR, SAMPLERZ_AXI__CONTROL__STOP__MASK, SAMPLERZ_AXI__CONTROL__STOP__MASK);
    endtask

    task samplerz_done(output bit done);
        axi_read_bit(SAMPLERZ_AXI__CONTROL__ADDR, done, SAMPLERZ_AXI__CONTROL__DONE__LSB);
    endtask

    task samplerz_full(output bit full);
        axi_read_bit(SAMPLERZ_AXI__CONTROL__ADDR, full, SAMPLERZ_AXI__CONTROL__RAND_FULL__LSB);
    endtask

    task samplerz_wait_done(input int timeout = 100);
        bit done;
        int i;
        for (i = 0; i < timeout; i++) begin
            samplerz_done(done);
            if (done) break;
            #1;
        end
        if (!done) begin
            $fatal(1, "Timeout waiting for done signal");
        end
    endtask

    task samplerz_wait_full(input int timeout = 100);
        bit full;
        int i;
        for (i = 0; i < timeout; i++) begin
            samplerz_full(full);
            if (full) break;
            #1;
        end
        if (!full) begin
            $fatal(1, "Timeout waiting for full signal");
        end
    endtask

    task samplerz_busy(output bit busy);
        axi_read_bit(SAMPLERZ_AXI__CONTROL__ADDR, busy, SAMPLERZ_AXI__CONTROL__BUSY__LSB);
    endtask

    task samplerz_print_status_axi();
        word_t control;
        double_t busy_cycles, consumed_bits, prng_counter;
        axi_read(SAMPLERZ_AXI__CONTROL__ADDR, control);
        axi_read2(SAMPLERZ_AXI__BUSY_CYCLES__ADDR, busy_cycles);
        axi_read2(SAMPLERZ_AXI__CONSUMED_BITS__ADDR, consumed_bits);
        axi_read2(SAMPLERZ_AXI__PRNG__COUNTER__ADDR, prng_counter);

        $display("=========================");
        $display("Control Register: %h (axi)", control);
        $display("  - FALCON1024: %b", control & SAMPLERZ_AXI__CONTROL__FALCON1024__MASK != 0);
        $display("  - START: %b", control & SAMPLERZ_AXI__CONTROL__START__MASK != 0);
        $display("  - STOP: %b", control & SAMPLERZ_AXI__CONTROL__STOP__MASK != 0);
        $display("  - DONE: %b", control & SAMPLERZ_AXI__CONTROL__DONE__MASK != 0);
        $display("  - CONTINUOUS: %b", control & SAMPLERZ_AXI__CONTROL__CONTINUOUS__MASK != 0);
        $display("  - RESET: %b", control & SAMPLERZ_AXI__CONTROL__RESET__MASK != 0);
        $display("  - BUSY: %b", control & SAMPLERZ_AXI__CONTROL__BUSY__MASK != 0);
        $display("  - RAND_FULL: %b", control & SAMPLERZ_AXI__CONTROL__RAND_FULL__MASK != 0);
        $display("Busy Cycles: %d", busy_cycles);
        $display("Consumed Bits: %d", consumed_bits);
        $display("PRNG Counter: 0x%h", prng_counter);
        $display("==========================");
    endtask

`define SAMPLERZ_TOP design_inst.design_axi_test_i.samplerz_axi_top_wra_0.inst.inst
`define HIGHLOW_VALUE(x) {x.high.value, x.low.value}

    task samplerz_print_status_sim();
        $display("=========================");
        $display("Control Register: (sim)");
        $display("  - FALCON1024: %b", `SAMPLERZ_TOP.axi.field_storage.control.falcon1024.value);
        $display("  - START: %b", `SAMPLERZ_TOP.axi.field_storage.control.start.value);
        $display("  - STOP: %b", `SAMPLERZ_TOP.axi.field_storage.control.stop.value);
        $display("  - DONE: %b", `SAMPLERZ_TOP.axi.hwif_in.control.done.next);
        $display("  - CONTINUOUS: %b", `SAMPLERZ_TOP.axi.field_storage.control.continuous.value);
        $display("  - RESET: %b", `SAMPLERZ_TOP.axi.field_storage.control.reset.value);
        $display("  - BUSY: %b", `SAMPLERZ_TOP.axi.hwif_in.control.busy.next);
        $display("  - RAND_FULL: %b", `SAMPLERZ_TOP.axi.hwif_in.control.rand_full.next);
        $display("Busy Cycles: %d", `HIGHLOW_VALUE(`SAMPLERZ_TOP.axi.field_storage.busy_cycles));
        $display("Consumed Bits: %d", `HIGHLOW_VALUE(`SAMPLERZ_TOP.axi.field_storage.consumed_bits));
        $display("PRNG Counter: 0x%h", `HIGHLOW_VALUE(`SAMPLERZ_TOP.axi.field_storage.prng.counter));
        $display("=========================");
    endtask

    task samplerz_read_samples(output word_t z1, z2);
        axi_read(SAMPLERZ_AXI__Z1__DATA__ADDR, z1);
        axi_read(SAMPLERZ_AXI__Z2__DATA__ADDR, z2);
    endtask

    task samplerz_print_histogram_axi(input int index);
        automatic double_t hist[SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__HISTOGRAM__ARRLEN];
        automatic word_t hist_pivot_value;
        automatic word_t hist_pivot_index;
        automatic double_t sum = 0;

        axi_read(
            SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__ADDR
            + index * SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__STRIDE
            + SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__PIVOT_INDEX__OFFSET,
            hist_pivot_index
        );
        axi_read(
            SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__ADDR
            + index * SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__STRIDE
            + SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__PIVOT_VALUE__OFFSET,
            hist_pivot_value
        );
        foreach (hist[i]) begin
            axi_read2(
                SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__ADDR
                + index * SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__STRIDE
                + SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__HISTOGRAM__OFFSET
                + i * SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__HISTOGRAM__STRIDE,
                hist[i]
            );
        end

        $display("Histogram of z%0d:", index+1);
        foreach (hist[i]) begin
            if (hist[i] != 0) begin
                sum += hist[i];
                $display("  %0d: %0d", signed'(hist_pivot_value) + signed'(i) - signed'(hist_pivot_index), hist[i]);
            end
        end
        $display("  Sum: %0d", sum);
    endtask;

    initial begin
        word_t data, z1, z2;
        localparam double_t sigma_inv = 64'h3FE21A5FD8ACCC85;
        localparam double_t mu1 = 64'h403770D850D3A641;
        localparam double_t mu2 = 64'hC04626A731D9A0CE;
         
        // localparam double_t sigma_inv = 64'h3FE4F074271C0184;
        // localparam double_t mu1 = 64'h4072651CCA2FCA40;
        // localparam double_t mu2 = 64'h4072651CCA2FCA40;

        // localparam double_t sigma_inv = $realtobits(0.588235);
        // localparam double_t mu1 = $realtobits(-1.0);
        // localparam double_t mu2 = $realtobits(-1.0);

        rst = 1;

        agent = new("samplerz_agent", design_inst.design_axi_test_i.axi_vip_0.inst.IF);
        agent.start_master();

        @(negedge clk);
        rst = 0;
        @(negedge clk);

        $display("Checking marker...");
        samplerz_check_marker();

        $display("Initializing PRNG...");
        samplerz_init_prng();

        $display("Resetting samplerz (clear out stale randomness)...");
        samplerz_reset();
        samplerz_wait_full();

        $display("Configuring samplerz...");
        samplerz_configure(.falcon1024(1), .continuous(0));

        $display("Setting samplerz parameters...");
        samplerz_params(
            .sigma_inv(sigma_inv),
            .mu1(mu1),
            .mu2(mu2)
        );

        samplerz_print_status_sim();
        samplerz_print_status_axi();

        $display("Starting samplerz...");
        samplerz_start();

        samplerz_print_status_sim();

        $display("Waiting for samplerz to complete...");
        samplerz_wait_done();

        samplerz_print_status_sim();

        $display("Reading samples z1 and z2...");
        samplerz_read_samples(z1, z2);

        $display("z1 = %d, z2 = %d", signed'(z1), signed'(z2));

        samplerz_wait_full();
        $display("The sampler is full of randomness again, check how many bits were used:");
        samplerz_print_status_sim();

        $display("Running in continuous mode...");
        samplerz_configure(.falcon1024(1), .continuous(1));
        samplerz_start();
        samplerz_print_status_sim();
        #200;
        samplerz_stop();
        samplerz_wait_full();
        samplerz_print_status_sim();

        samplerz_print_histogram_axi(0);
        samplerz_print_histogram_axi(1);

        $display("All done!");
        $finish;
    end
endmodule
