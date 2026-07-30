
module parallel_to_serial #(
    parameter W = 8,
    parameter DEPTH = 2, // number of refill FIFO stages

    localparam W_BITS = $clog2(W)
)(
    input logic clk, rst,

    input logic [W-1:0] refill,
    input logic  refill_valid,
    output logic refill_req,
    output logic full,

    output logic out,
    output logic out_valid,
    input  logic used
);

    logic [W-1:0] shiftreg;
    logic [W-1:0] buffers [0:DEPTH-1];
    logic [DEPTH-1:0] buffers_full;
    logic [W_BITS:0] count;

    assign out = shiftreg[0];
    assign out_valid = count != 0;
    assign refill_req = ~(&(buffers_full)) || (count == 0) || (count == 1 && used); // refill if any buffers empty, if SR is empty or about to be empty
    assign full = buffers_full[DEPTH-1];

    always_ff @(posedge clk) begin
        if (count != 0 && used) begin
            count = count - 1;
            shiftreg = shiftreg >> 1;
            shiftreg[W-1] = 'X; // for simulation
        end

        if (count == 0 && buffers_full[0]) begin
            shiftreg = buffers[0];
            for (int i = 0; i < DEPTH-1; i++) begin
                buffers[i] = buffers[i+1];
                buffers_full[i] = buffers_full[i+1];
            end
            count = W;
            buffers_full[DEPTH-1] = 0;
            buffers[DEPTH-1] = 'X; // for simulation
        end

        if (count == 0 && refill_valid) begin
            // direct path to shifteg
            shiftreg = refill;
            count = W;
        end else begin
            // try to fill any buffer
            for (int i = 0; i < DEPTH; i++) begin
                if (!buffers_full[i] && refill_valid) begin
                    buffers[i] = refill;
                    buffers_full[i] = 1;
                    break;
                end
            end
        end

        if (rst) begin
            count = 0;
            buffers_full = 0;
            foreach (buffers[i]) buffers[i] = 'X; // for simulation
            shiftreg = 'X; //sim
        end
    end
endmodule