`timescale 1ns/1ps

module refill_uniform_buf_tb;
    localparam OUT_W = 10;
    localparam OUT_W_BITS = $clog2(OUT_W);
    localparam REFILL_W = 4;
    localparam HOT_BITS = 2;
    localparam HOT_BITS_DEPTH = 2;
    localparam FAST_BUFS = 1;

    logic clk, rst;

    // refill interface
    refill_if #(REFILL_W) refill_port();
    logic [REFILL_W-1:0] refill;
    logic refill_valid;
    logic refill_req;
    logic full;
    assign refill_port.source.refill = refill;
    assign refill_port.source.refill_valid = refill_valid;
    assign refill_req = refill_port.source.refill_req;
    assign full = refill_port.source.full;

    logic [OUT_W-1:0] out;
    logic out_valid;
    logic [OUT_W_BITS-1:0] used_bits;
    logic used;

    refill_uniform_buf #(
        .OUT_W(OUT_W),
        // .REFILL_W(REFILL_W),
        .HOT_BITS(HOT_BITS),
        .HOT_BITS_DEPTH(HOT_BITS_DEPTH),
        .FAST_BUFS(FAST_BUFS)
    ) dut (
        .clk(clk), .rst(rst),
        .refill_port(refill_port.sink),
        // .refill(refill),
        // .refill_valid(refill_valid),
        // .refill_req(refill_req),
        // .full(full),
        .out(out),
        .out_valid(out_valid),
        .used_bits(used_bits),
        .used(used)
    );

    localparam NREFILLS = 10;
    logic [REFILL_W-1:0] the_refills [0:NREFILLS-1] = '{
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    };

    always #1 clk = ~clk;

    initial begin
        clk = 0;
        rst = 1;
        refill = 0;
        refill_valid = 0;
        used_bits = 0;
        used = 0;

        @(negedge clk);
        @(negedge clk);
        rst = 0;

        @(negedge clk);
        assert(refill_req == 1 && full == 0 && out_valid == 0) else $error("post reset check");

        // refill all
        for (int i = 0; i < NREFILLS; i++) begin
            refill = the_refills[i];
            refill_valid = 1;

            assert(refill_req == 1 && full == 0 && out_valid == 0) else $error("pre refill %0d check", i);
            @(negedge clk);
        end
        refill_valid = 0;
        assert(refill_req == 0 && full == 1 && out_valid == 1) else $error("post fill check");

        @(negedge clk); //===============================================================

        // start consuming some bits
        assert(out_valid == 1 && out == 'b1001_0111_01) else $error("consume 1");
        used_bits = 7;
        used = 1;

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 1");
        // into refill_buf 0
        refill_valid = 1;
        refill = 11;

        assert(out_valid == 1 && out == 'b1010_1000_00) else $error("consume 2");
        used_bits = 10;
        used = 1;

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 2 no");
        // do not refill
        refill_valid = 0;

        assert(out_valid == 0) else $error("invalid 1");
        used_bits = 7; // should have no effect
        used = 0;

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 3");
        // into refill_buf 1
        refill_valid = 1;
        refill = 12;

        assert(out_valid == 0) else $error("invalid 2");

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 4");
        // into refill_buf 1
        refill_valid = 1;
        refill = 13;

        assert(out_valid == 0) else $error("invalid 3");

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 5");
        // into refill_buf 1
        refill_valid = 1;
        refill = 14;

        assert(out_valid == 0) else $error("invalid 4");

        @(negedge clk); //===============================================================

        assert(refill_req == 0 && full == 1) else $error("full 1");
        refill_valid = 0;
        refill = 'X; // should not be used!!

        assert(out_valid == 1 && out == 'b1101_1011_10) else $error("consume 3");
        used_bits = 6;
        used = 1;

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 6 no");
        // do not refill
        refill_valid = 0;
        refill = 15;

        assert(out_valid == 1 && out == 'b1101_1100_00) else $error("consume 4");
        used_bits = 2;
        used = 1;

        @(negedge clk); //===============================================================
        
        assert(refill_req == 1 && full == 0) else $error("refill 7");

        // into hot 0
        refill_valid = 1;
        refill = 15;

        assert(out_valid == 1 && out == 'b1101_1100_10) else $error("consume 5");
        used_bits = 3;
        used = 1;

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 8");
        // into hot 1
        refill_valid = 1;
        refill = 0;

        assert(out_valid == 0) else $error("invalid 5");
        used_bits = 0;
        used = 0;

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 9");
        // into out buf 0
        refill_valid = 1;
        refill = 1;

        assert(out_valid == 0) else $error("invalid 6");
        used_bits = 0;
        used = 0;

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 10");
        // into refill buf 1
        refill_valid = 1;
        refill = 2;

        assert(out_valid == 1 && out == 'b1101_0001_01) else $error("consume 6");
        used_bits = 1;
        used = 1;

        @(negedge clk); //===============================================================

        assert(refill_req == 0 && full == 1) else $error("full 2");
        refill_valid = 1;
        refill = 'X; // should not be used!!

        assert(out_valid == 1 && out == 'b1101_0001_00) else $error("consume 7");
        used_bits = 8;
        used = 1;

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 11 no");
        // do not refill
        refill_valid = 0;
        refill = 3;

        assert(out_valid == 1 && out == 'b1110_0010_10) else $error("consume 8");
        used_bits = 2;
        used = 0; // leave one cycle out

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 12 no");
        // do not refill
        refill_valid = 0;
        refill = 4;

        assert(out_valid == 1 && out == 'b1110_0010_10) else $error("consume 9");
        used_bits = 2;
        used = 1;

        @(negedge clk); //===============================================================

        assert(refill_req == 1 && full == 0) else $error("refill 13 no");
        // do not refill
        refill_valid = 0;
        refill = 5;

        assert(out_valid == 1 && out == 'b1110_0010_01) else $error("consume 10");
        used_bits = 2;
        used = 1;

        @(negedge clk); //===============================================================
        assert(out_valid == 1 && out == 'b1110_0010_01) else $error("consume 11");
        used_bits = 1;
        @(negedge clk);
        assert(out_valid == 1 && out == 'b1110_0010_00) else $error("consume 12");
        @(negedge clk);
        assert(out_valid == 1 && out == 'b1110_0010_00) else $error("consume 13");
        @(negedge clk);
        assert(out_valid == 1 && out == 'b1110_0010_01) else $error("consume 14");
        @(negedge clk);
        assert(out_valid == 1 && out == 'b1110_0010_01) else $error("consume 15");
        @(negedge clk);
        assert(out_valid == 1 && out == 'b1110_0010_01) else $error("consume 16");
        @(negedge clk);
        assert(out_valid == 1 && out == 'b1110_0010_01) else $error("consume 17");
        @(negedge clk);
        assert(out_valid == 0) else $error("invalid 7");
        used_bits = 0;
        used = 0;
        @(negedge clk); //===============================================================
        assert(refill_req == 1 && full == 0) else $error("refill 14 no");

        $finish;
    end
endmodule
