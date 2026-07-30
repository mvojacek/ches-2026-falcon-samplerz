`timescale 1ns / 1ps

module float_fractional_tb;

  logic [63:0] in, out, n, ex, n_ex;
  logic clk = 0, err = 0, n_err = 0, failed = 0;

  fp_int_frac #(
    .INT_W(64)
  ) dut (
      .in(in),
      .out_frac(out),
      .out_int(n)
  );

  always #1 clk = ~clk;
  always_comb err = out != ex;
  always_comb n_err = n != n_ex;

  localparam NO_NEGATIVE = 1;
  localparam NO_SUBNORMAL = 1;

  logic valid_test;
  assign valid_test = !((NO_NEGATIVE && in[63] == 1) || (NO_SUBNORMAL && in[62:52] == 0 && (|in[51:0]) != 0));
  
  int count_total = 0;
  int count_passed = 0;
  int count_ignored = 0;
  int count_failed = 0;

  always @(negedge clk) begin
    count_total += 1;
    if (valid_test) begin
      if (err || n_err) begin
        $display("Test failed: in=%h, out=%h, ex=%h, n=%h, n_ex=%h", in, out, ex, n, n_ex);
        failed = 1;
        count_failed += 1;
      end else begin
        count_passed += 1;
      end
    end else begin
      count_ignored += 1;
    end
  end

  initial begin
// Test case: 0.8554694521841739 = 0 + 0.8554694521841739
in   = 64'b0011111111101011011000000000000101111000111110110111010101000000;
ex   = 64'b0011111111101011011000000000000101111000111110110111010101000000;
n_ex = 64'd0;
@(posedge clk);
@(posedge clk);

// Test case: -0.10374917341039769 = -1 + 0.8962508265896023
in   = 64'b1011111110111010100011110100111001001010110010001110000110000000;
ex   = 64'b0011111111101100101011100001011000110110101001101110001111010000;
n_ex = -64'd1;
@(posedge clk);


`include "data/float_fractional_samplerzkat_testcases.sv"

`include "data/float_fractional_testcases.sv"

    $display("passed %0d, failed %0d, ignored %0d", count_passed, count_failed, count_ignored);
    if (failed) $display("Test failed");
    else $display("All tests passed");
    $finish;
  end
endmodule
