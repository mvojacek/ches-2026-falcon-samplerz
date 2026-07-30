module refill_fastbufs3 #(
    parameter OUT_W = 64,
    localparam OUT_W_BITS = $clog2(OUT_W)
    // // parameter REFILL_W = 8,
    // parameter HOT_BITS = 5, // must be at least 1, and less is not useful anyway
    // parameter HOT_BITS_DEPTH = 2, // the hot bits dispensers have an internal fifo to avoid stalls
    // parameter FAST_BUFS = 3 // the number of buffers which can be refilled without creating a bubble if two values are consumed back-to-back
)(
    input clk, rst,
    
    // input logic [REFILL_W-1:0] refill,
    // input logic refill_valid,
    // output logic refill_req,
    // output logic full,
    refill_if.sink refill_port,
    
    output logic [OUT_W-1:0] out,
    output logic out_valid,
    input  logic [OUT_W_BITS-1:0] used_bits,
    input  logic used
);
    refill_uniform_buf #(
        .OUT_W(OUT_W),
        .HOT_BITS(5),
        .HOT_BITS_DEPTH(1),
        .FAST_BUFS(1)
    ) refill_uniform_buf_inst (
        .clk(clk),.rst(rst),
        .refill_port(refill_port),
        .out(out),
        .out_valid(out_valid),
        .used_bits(used_bits),
        .used(used)
    ); 

endmodule