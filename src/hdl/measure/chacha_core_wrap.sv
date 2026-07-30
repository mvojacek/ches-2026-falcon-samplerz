module chacha_core_wrap(
    input logic clk,
    input logic rst,
    input logic init,
    input logic [255:0] key,
    input logic [63:0] iv,
    input logic [63:0] ctr,
    output logic ready,
    output logic [511:0] data_out,
    output logic data_out_valid
);

    chacha_core chacha_inst (
        .clk(clk),
        .reset_n(~rst),
        .init(init),
        .next('0),
        .key(key),
        .keylen('b1),
        .iv(iv),
        .ctr(ctr),
        .rounds('d20),
        .data_in('0),
        .ready(ready),
        .data_out(data_out),
        .data_out_valid(data_out_valid)
    );

endmodule
