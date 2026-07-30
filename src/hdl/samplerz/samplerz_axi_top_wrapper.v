`timescale 1ns/1ps

module samplerz_axi_top_wrapper #(
    parameter AXI_DATA_WIDTH = 32,
    parameter AXI_ADDR_WIDTH = 40
)(
    input wire aclk,
    input wire aresetn,
    // === AXI-4 Lite slave ===
    output wire AWREADY,
    input wire AWVALID,
    input wire [AXI_ADDR_WIDTH-1:0] AWADDR,
    input wire [2:0] AWPROT,

    output wire WREADY,
    input wire WVALID,
    input wire [AXI_DATA_WIDTH-1:0] WDATA,
    input wire [AXI_DATA_WIDTH/8-1:0] WSTRB,

    input wire BREADY,
    output wire BVALID,
    output wire [1:0] BRESP,

    output wire ARREADY,
    input wire ARVALID,
    input wire [AXI_ADDR_WIDTH-1:0] ARADDR,
    input wire [2:0] ARPROT,

    input wire RREADY,
    output wire RVALID,
    output wire [AXI_DATA_WIDTH-1:0] RDATA,
    output wire [1:0] RRESP
);

    (* keep_hierarchy = "yes" *)
    samplerz_axi_top #(
        .AXI_DATA_WIDTH(AXI_DATA_WIDTH),
        .AXI_ADDR_WIDTH(AXI_ADDR_WIDTH)
    ) inst (
        .aclk(aclk),
        .aresetn(aresetn),
        .AWREADY(AWREADY),
        .AWVALID(AWVALID),
        .AWADDR(AWADDR),
        .AWPROT(AWPROT),
        .WREADY(WREADY),
        .WVALID(WVALID),
        .WDATA(WDATA),
        .WSTRB(WSTRB),
        .BREADY(BREADY),
        .BVALID(BVALID),
        .BRESP(BRESP),
        .ARREADY(ARREADY),
        .ARVALID(ARVALID),
        .ARADDR(ARADDR),
        .ARPROT(ARPROT),
        .RREADY(RREADY),
        .RVALID(RVALID),
        .RDATA(RDATA),
        .RRESP(RRESP)
    );

endmodule
