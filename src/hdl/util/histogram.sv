`timescale 1ns/1ps

// Hardware histogram with pivot. The first sample is always placed in the middle bin.
// Allocate enough bins to cover the full range of samples 
module histogram #(
    parameter BINS = 40,
    parameter BIN_W = 64,
    parameter SAMPLE_W = 32,
    
    localparam BINS_BITS = $clog2(BINS),
    localparam PIVOT_BIN = BINS / 2,
    localparam BINS_BEFORE = PIVOT_BIN,
    localparam BINS_AFTER = BINS - PIVOT_BIN - 1
)(
    input logic clk, rst,
    input logic [SAMPLE_W-1:0] sample,
    input logic sample_valid,

    output logic bounds_error,
    output logic [BIN_W-1:0] hist [BINS],
    output logic [SAMPLE_W-1:0] hist_pivot_value,
    output logic [BINS_BITS-1:0] hist_pivot_index
);

logic hist_middle_valid;

logic signed [SAMPLE_W-1:0] sample_offset;
assign sample_offset = sample - hist_pivot_value;

always_ff @(posedge clk) begin
    if (rst) begin
        hist_middle_valid <= 1'b0;
        hist_pivot_value <= '0;
        hist_pivot_value <= '0;
        hist <= '{default: '0};
        bounds_error <= 1'b0;
    end else if (sample_valid) begin
        if (hist_middle_valid) begin
            if (sample_offset < -BINS_BEFORE || sample_offset > BINS_AFTER) begin
                bounds_error <= 1'b1;
            end else begin
                hist[PIVOT_BIN + sample_offset] <= hist[PIVOT_BIN + sample_offset] + 1;
            end
        end else begin
            hist[PIVOT_BIN] <= hist[PIVOT_BIN] + 1;
            hist_pivot_value <= sample;
            hist_middle_valid <= 1'b1;
        end
    end
end

assign hist_pivot_index = PIVOT_BIN;

endmodule
