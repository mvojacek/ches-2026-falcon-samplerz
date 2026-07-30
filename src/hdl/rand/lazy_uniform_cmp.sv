
// compares the value with a uniform sample and report how many bits were needed to make the decision
// uniform bits are consumed from MSB direction (as you would expect with a compare)
// input is 1 bit larger to allow 100% chance of success
module lazy_uniform_cmp #(
    parameter W = 64,
    localparam W_BITS = $clog2(W)
)(
    input logic [W:0] in,
    input logic [W-1:0] uniform,
    output logic in_gt, in_lt, eq,
    output logic [W_BITS-1:0] used_bits
);
    always_comb begin
        in_gt = 0;
        in_lt = 0;
        eq = 1;
        used_bits = W;
        for (int i = 1; i <= W; i++) begin
            if (in[W-i] != uniform[W-i]) begin
                in_gt = in[W-i];
                in_lt = uniform[W-i];
                eq = 0;
                used_bits = i;
                break;
            end
        end

        if (in[W] == 1) begin
            in_gt = 1;
            in_lt = 0;
            eq = 0;
            used_bits = 0; // 100% chance
        end
    end
endmodule

module lazy_uniform_cmp_reg #( // @suppress "File contains multiple design units"
    parameter W = 64,
    localparam W_BITS = $clog2(W)
)(
    input logic clk,
    input logic [W:0] in,
    input logic [W-1:0] uniform,
    output logic in_gt,
    output logic [W_BITS-1:0] used_bits
);
    logic [W:0] _in;
    logic [W-1:0] _uniform;
    logic _in_gt;
    logic [W_BITS-1:0] _used_bits;

    lazy_uniform_cmp #(.W(W)) inst (
        .in(_in),
        .uniform(_uniform),
        .in_gt(_in_gt), .in_lt(), .eq(),
        .used_bits(_used_bits)
    );

    always_ff @(posedge clk) begin
        _in <= in;
        _uniform <= uniform;
        in_gt <= _in_gt;
        used_bits <= _used_bits;
    end
endmodule
