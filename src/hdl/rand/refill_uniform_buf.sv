`timescale 1ns / 1ps

interface refill_if #(
    parameter REFILL_W = 8
);
    logic [REFILL_W-1:0] refill;
    logic refill_valid;
    logic refill_req;
    logic full;

    modport sink (input refill, input refill_valid, output refill_req, output full);
    modport source (output refill, output refill_valid, input refill_req, input full);
endinterface

// Using the refill* ports, this module requests REFILL_W bits from a source when needed.
// If out_valid=1, the the out port is fully uniformly random.
// Ff any of those bits are used, it must be reported with used=1 and used_bits=N of LSB bits used.
// The module has an internal buffer to accomodate consumption each cycle.
// A HOT_BITS amount of LSB bits are refilled independently serially, the rest are (wastefully) refilled in REFILL_W blocks
module refill_uniform_buf #(
    parameter OUT_W = 64,
    localparam OUT_W_BITS = $clog2(OUT_W),
    // parameter REFILL_W = 8,
    parameter HOT_BITS = 5, // must be at least 1, and less is not useful anyway
    parameter HOT_BITS_DEPTH = 2, // the hot bits dispensers have an internal fifo to avoid stalls
    parameter FAST_BUFS = 3 // the number of buffers which can be refilled without creating a bubble if two values are consumed back-to-back
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
    // get wires from interface
    localparam REFILL_W = refill_port.REFILL_W;
    logic [REFILL_W-1:0] refill_val;
    logic refill_valid;
    logic refill_req;
    logic full;
    assign refill_val = refill_port.refill;
    assign refill_valid = refill_port.refill_valid;
    assign refill_port.refill_req = refill_req;
    assign refill_port.full = full;

    logic [HOT_BITS-1:0] do_hot_refill, hot_refill_req, hot_full, hot_out, hot_out_valid, hot_used;

    // for each hot bit, generate a parallel to serial converter
    genvar i;
    generate
        for (i = 0; i < HOT_BITS; i++) begin : hotbits
            parallel_to_serial #(
                .W(REFILL_W),
                .DEPTH(HOT_BITS_DEPTH)
            ) par2ser (
                .clk(clk),.rst(rst),
                .refill(refill_val),
                .refill_valid(do_hot_refill[i]),
                .refill_req(hot_refill_req[i]),
                .full(hot_full[i]),
                .out(hot_out[i]),
                .out_valid(hot_out_valid[i]),
                .used(hot_used[i])
            );
        end
    endgenerate

    // calculate which hot bits are used
    always_comb begin
        for (int i = 0; i < HOT_BITS; i++) begin
            hot_used[i] = (used_bits > i) && used;
        end
    end
    
    // refill other bits from buffers
    localparam N = (OUT_W-HOT_BITS+REFILL_W-1) / REFILL_W; // ceil((OUT_W-PROBABLE_BITS)/REFILL_W)
    logic [REFILL_W-1:0] refill_buf [0:N-1];
    logic [REFILL_W-1:0] out_buf    [0:N-1];
    logic [N-1:0] refill_buf_valid, refill_buf_req, out_buf_valid, out_buf_used, do_buf_refill;

    always_comb begin
        for (int i = 0; i < N; i++) begin
            // calculate which bufs are used
            out_buf_used[i] = (used_bits > (HOT_BITS + i*REFILL_W)) && used;
            // refill request when either buf is not valid or it is being used
            refill_buf_req[i] = ~refill_buf_valid[i] || ~out_buf_valid[i] || out_buf_used[i];
        end
    end

    always_ff @(posedge clk) begin
        for (int i = 0; i < N; i++) begin
            // consume buf
            if (out_buf_valid[i] && out_buf_used[i]) begin
                out_buf_valid[i] = 0;
                out_buf[i] = 'X; // for simulation
            end

            // if refill is avilable, refill
            if (refill_buf_valid[i] && !out_buf_valid[i]) begin
                out_buf[i] = refill_buf[i];
                refill_buf_valid[i] = 0;
                out_buf_valid[i] = 1;
                refill_buf[i] = 'X; // for simulation
            end

            // refill from parent if available
            if (do_buf_refill[i] && !refill_buf_valid[i]) begin
                if (i < FAST_BUFS && !out_buf_valid[i]) begin
                    // prevent bubble
                    out_buf[i] = refill_val;
                    out_buf_valid[i] = 1;
                end else begin
                    // regular fifo
                    refill_buf[i] = refill_val;
                    refill_buf_valid[i] = 1;
                end
            end
        end

        if (rst) begin
            out_buf_valid = 0;
            refill_buf_valid = 0;
            foreach (out_buf[i]) out_buf[i] = 'X; //sim
            foreach (refill_buf[i]) refill_buf[i] = 'X; //sim
        end
    end

    // arbitrate refill - priority on low 
    always_comb begin
        do_hot_refill = 0;
        do_buf_refill = 0;

        if (refill_valid) begin
            for (int i = 0; i < HOT_BITS + N; i++) begin
                if (i < HOT_BITS) begin
                    if (hot_refill_req[i]) begin
                        do_hot_refill[i] = 1;
                        break;
                    end
                end else begin
                    if (refill_buf_req[i-HOT_BITS]) begin
                        do_buf_refill[i-HOT_BITS] = 1;
                        break;
                    end
                end
            end
        end
    end

    // output
    (* keep="soft" *) logic [(REFILL_W*N)-1:0] out_buf_1d;
    assign out_buf_1d = {<<REFILL_W{out_buf}}; // MSB bits are truncated, not used and should be optimized away
    assign out = {out_buf_1d[0+:OUT_W-HOT_BITS], hot_out}; 
    // assign out_valid = &(hot_out_valid | ~hot_used) && &(out_buf_valid | ~out_buf_used); // only invalid if an invalid buffer is also used
    assign out_valid = &(hot_out_valid) && &(out_buf_valid);
    assign full = &(hot_full) && &(refill_buf_valid) && &(out_buf_valid);
    assign refill_req = |(hot_refill_req) || |(refill_buf_req);
endmodule
