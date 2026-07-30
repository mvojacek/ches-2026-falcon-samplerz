`timescale 1ns / 1ps

// Leading Zeros Counter
module lz_counter #(
    parameter WIDTH = 52
) (
    input logic [WIDTH-1:0] data_in,
    output logic [$clog2(WIDTH)-1:0] leading_zeros
);
  always_comb begin
    leading_zeros = WIDTH;  // default case, 
    for (int i = 0; i < WIDTH; i++) begin
      if (data_in[WIDTH-1-i] == 1) begin
        leading_zeros = i;
        break;
      end
    end
  end
endmodule
