`timescale 1ns / 1ps

module fp_int_frac_z_tb;

  logic [63:0] in, out, n, ex, n_ex;
  logic clk = 0, err = 0, n_err = 0, failed = 0;

  fp_int_frac_z #(
    .INT_W(64)
  ) dut (
      .in(in),
      .out_frac(out),
      .out_int(n)
  );

  always #1 clk = ~clk;
  always_comb err = out != ex;
  always_comb n_err = n != n_ex;

  localparam NO_NEGATIVE = 0; // Negative tests ENABLED
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
        $display("Test failed at time %t: in=%h, out=%h (ex=%h), n=%h (ex=%h)", $time, in, out, ex, n, n_ex);
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
    // Use relative paths assuming run from repo root
    `include "src/sim/data/float_fractional_samplerzkat_testcases.sv"
    `include "src/sim/data/float_fractional_testcases.sv"

    $display("passed %0d, failed %0d, ignored %0d", count_passed, count_failed, count_ignored);
    if (failed) $display("Test failed");
    else $display("All tests passed");
    $finish;
  end
endmodule
