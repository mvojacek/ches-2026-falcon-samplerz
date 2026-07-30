
import samplerz_axi_pkg::*;
import samplerz_pkg::*;
import fp_pkg::*;
import samplerz_axi_map_pkg::SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__HISTOGRAM__ARRLEN;

module samplerz_axi_top #(
    parameter AXI_DATA_WIDTH = 32,
    parameter AXI_ADDR_WIDTH = 40
)(
    input logic aclk, aresetn,
    // === AXI-4 Lite slave ===
    output logic AWREADY,
    input logic AWVALID,
    input logic [AXI_ADDR_WIDTH-1:0] AWADDR,
    input logic [2:0] AWPROT,

    output logic WREADY,
    input logic WVALID,
    input logic [AXI_DATA_WIDTH-1:0] WDATA,
    input logic [AXI_DATA_WIDTH/8-1:0] WSTRB,

    input logic BREADY,
    output logic BVALID,
    output logic [1:0] BRESP,

    output logic ARREADY,
    input logic ARVALID,
    input logic [AXI_ADDR_WIDTH-1:0] ARADDR,
    input logic [2:0] ARPROT,

    input logic RREADY,
    output logic RVALID,
    output logic [AXI_DATA_WIDTH-1:0] RDATA,
    output logic [1:0] RRESP
);

    axi4lite_intf #(
        .DATA_WIDTH(AXI_DATA_WIDTH),
        .ADDR_WIDTH(AXI_ADDR_WIDTH)
    ) axi_if ();

    assign AWREADY = axi_if.AWREADY;
    assign axi_if.AWVALID = AWVALID;
    assign axi_if.AWADDR = AWADDR;
    assign axi_if.AWPROT = AWPROT;
    assign WREADY = axi_if.WREADY;
    assign axi_if.WVALID = WVALID;
    assign axi_if.WDATA = WDATA;
    assign axi_if.WSTRB = WSTRB;
    assign axi_if.BREADY = BREADY;
    assign BVALID = axi_if.BVALID;
    assign BRESP = axi_if.BRESP;
    assign ARREADY = axi_if.ARREADY;
    assign axi_if.ARVALID = ARVALID;
    assign axi_if.ARADDR = ARADDR;
    assign axi_if.ARPROT = ARPROT;
    assign axi_if.RREADY = RREADY;
    assign RVALID = axi_if.RVALID;
    assign RDATA = axi_if.RDATA;
    assign RRESP = axi_if.RRESP;

    samplerz_axi__in_t out; // direction inversion - for us they are outputs
    samplerz_axi__out_t in;

`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    samplerz_axi axi(
        .clk(aclk),
        .rst(~aresetn),
        .s_axil(axi_if.slave),
        .hwif_in(out),
        .hwif_out(in)
    );

    localparam REFILL_W = 8;
    localparam REFILL_PORTS = 3;

    logic [32*11-1:0] seed;
    always_comb begin
        for (int i = 0; i < 11; i++) begin
            seed[i*32+:32] = in.prng.seed[i].data.value;
        end
    end

    refill_if refills[REFILL_PORTS]();

`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    prng_refill #(
        .REFILL_W(REFILL_W),
        .REFILL_PORTS(REFILL_PORTS)
    ) prng (
        .clk(aclk),
        .rst(~aresetn || in.control.reset.value),
        .seed(seed),
        .counter({in.prng.counter.high.value, in.prng.counter.low.value}),
        .counter_use(out.prng.counter.low.incr),
        .refill(refills)
    );

    logic [REFILL_PORTS-1:0] refills_used;
    genvar i;
    generate
        for (i = 0; i < REFILL_PORTS; i++) begin : refill_used
            assign refills_used[i] = refills[i].refill_req && refills[i].refill_valid;
        end
    endgenerate

    logic start, continuous, stop, busy, full;
    mu_int_t sample_z [2];
    logic sample_z_valid [2];

    logic [$clog2(REFILL_PORTS)-1:0] refill_used_words;
    logic [31:0] refill_used_bits;
    always_comb begin
        refill_used_words = '0;
        for (int i = 0; i < REFILL_PORTS; i++) begin
            refill_used_words += refills_used[i];
        end
        refill_used_bits = refill_used_words * REFILL_W;
    end
    assign out.consumed_bits.low.incrvalue = refill_used_bits;
    assign out.consumed_bits.low.incr = 1'b1;
    assign out.consumed_bits.reset_consumed_bits = start || ~aresetn;

    assign start = in.control.start.value;
    assign continuous = in.control.continuous.value;
    assign stop = in.control.stop.value;

    assign out.control.rand_full.next = full;
    assign out.control.busy.next = busy;
    assign out.busy_cycles.low.incr = busy;
    assign out.busy_cycles.reset_busy_cycles = start || ~aresetn;

    assign out.z1.data.next = sample_z[0];
    assign out.z2.data.next = sample_z[1];

    fp_t sginv, mu1, mu2, mu;
    assign sginv = {in.sginv.high.value, in.sginv.low.value};
    assign mu1 = {in.mu1.high.value, in.mu1.low.value};
    assign mu2 = {in.mu2.high.value, in.mu2.low.value};
    assign mu = start ? mu1 : mu2;

`ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    samplerz samplerz_inst(
        .clk(aclk),
        .rst(~aresetn || in.control.reset.value),
        .falcon1024(in.control.falcon1024.value),
        .mu(mu),
        .start(start),
        .continuous(continuous),
        .stop(stop),
        .busy(busy),
        .sigma_inv(sginv),
        .sigma_inv_valid(start), // set ccs concurrently with mu1
        .sample_z1(sample_z[0]),
        .sample_z2(sample_z[1]),
        .sample_z1_valid(sample_z_valid[0]),
        .sample_z2_valid(sample_z_valid[1]),
        .done(out.control.done.next),
        .refill_exp(refills[0].sink),
        .refill_ccs(refills[1].sink),
        .refill_basesampler(refills[2].sink),
        .full(full)
    );

    genvar j;
    generate
        for (j = 0; j < 2; j++) begin : histograms
            logic bounds_error;
            logic [63:0] hist [SAMPLERZ_AXI__SAMPLE_HISTOGRAMS__HISTOGRAM__ARRLEN];
            mu_int_t hist_pivot_value;
            logic [$clog2($size(hist))-1:0] hist_pivot_index;
`ifdef SZ_KEEP_HIERARCHY
            (* keep_hierarchy = "yes" *)
`endif
            histogram #(
                .BINS($size(hist)),
                .BIN_W($bits(hist[0])),
                .SAMPLE_W($bits(sample_z[j]))
            ) hist_inst (
                .clk(aclk),
                .rst(~aresetn || in.control.reset.value || in.control.start.value),
                .sample(sample_z[j]),
                .sample_valid(sample_z_valid[j]),
                .bounds_error(bounds_error),
                .hist(hist),
                .hist_pivot_value(hist_pivot_value),
                .hist_pivot_index(hist_pivot_index)
            );

            always_comb begin
                foreach (hist[i]) begin
                    out.sample_histograms[j].histogram[i].low.next = hist[i][31:0];
                    out.sample_histograms[j].histogram[i].high.next = hist[i][63:32];
                end
                out.sample_histograms[j].pivot_value.data.next = hist_pivot_value;
                out.sample_histograms[j].pivot_index.data.next = hist_pivot_index;
            end
        end
    endgenerate
endmodule
