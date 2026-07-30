`timescale 1ns/1ps

module i2f_small_tb;

  localparam INT_W = 10;

  logic [INT_W-1:0] in;
  logic             sign;
  logic [63:0]      actual;
  logic [63:0]      expected;

  i2f_small #(
    .INT_W(INT_W),
    .FRAC_W(52),
    .EXP_W(11),
    .EXP_BIAS(11'h3FF)
  ) dut (
    .in(in),
    .sign(sign),
    .out(actual)
  );

  function automatic logic [63:0] int_to_double(
    input logic [INT_W-1:0] in_val,
    input logic sign_val
);
    real r = sign_val && in_val != 0 ? -$itor(in_val) : $itor(in_val);
    return $realtobits(r);
  endfunction


  initial begin
    int total = 0, passed = 0;
    for (int s = 0; s < 2; s++) begin
      for (int i = 0; i < (1 << INT_W); i++) begin
        in   = i;
        sign = s;
        expected = int_to_double(in, sign);
        #1;
        total++;
        if (actual !== expected) begin
          $display("FAIL: in=%0d sign=%0b\n| exp=%b \n| got=%b", in, sign, expected, actual);
        end else begin
          passed++;
        end
      end
    end
    $display("64-bit float test complete. Passed %0d / %0d", passed, total);
    $finish;
  end
endmodule
