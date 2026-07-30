`timescale 1ns/1ps

module fake_refill(
    refill_if.source refill
);

    assign refill.refill_valid = 1;
    assign refill.refill = 0;

endmodule

module urandom_refill(
    input clk,
    refill_if.source refill
);

    function logic[7:0] random8;
        automatic logic[31:0] r = $urandom ^ $urandom;
        return r[0+:8] ^ r[8+:8] ^ r[16+:8] ^ r[24+:8];
    endfunction

    assign refill.refill_valid = 1;

    always_ff @(posedge clk) begin
        refill.refill <= random8();
    end

endmodule

module file_refill #(
    parameter string FILE = "refill.txt"
)(
    input logic clk,
    refill_if.source refill
);
    initial begin
        assert (refill.REFILL_W == 8)
        else $fatal(1, "file_refill: refill must be 8 bits wide.");
    end

    int file, r;
    logic [7:0] next_value;

    initial begin
        file = $fopen(FILE, "rb");
        if (!file) $fatal(1, "file_refill: Failed to open file %s", FILE);
    end

    always_ff @(posedge clk) begin
        r = $fread(next_value, file);
        if (r != 1) begin
            $display("file_refill: EOF or read error");
            refill.refill <= 'X;
            refill.refill_valid <= 0;
        end
        refill.refill <= next_value;
        refill.refill_valid <= 1;
    end
endmodule
