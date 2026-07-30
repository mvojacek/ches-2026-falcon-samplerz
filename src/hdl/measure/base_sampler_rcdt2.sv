module base_sampler_rcdt2(
    input logic clk, rst,
    input logic [71:0] uniform,
    output logic [4:0] sample_out,
    output logic valid
);

    logic cycle;
    always_ff @(posedge clk) cycle <= rst ? 0 : ~cycle;

    logic [8:0] cmps;
    always_comb begin
        if (cycle == 0) begin
            cmps[0] = uniform < 72'b101000111111011111110100001011101101001110101100001110010001100000000010;
            cmps[1] = uniform < 72'b010101001101001100101011000110000001111100111111011111011101101110000010;
            cmps[2] = uniform < 72'b001000100111110111001101110100001001001101001000001010011100000111111111;
            cmps[3] = uniform < 72'b000010101101000101110101010000110111011111000111100110010100101011100100;
            cmps[4] = uniform < 72'b000000101001010110000100011011001010111011110011001111110001111101101111;
            cmps[5] = uniform < 72'b000000000111011101001010110001110101010011101101011101001011110101011111;
            cmps[6] = uniform < 72'b000000000001000000100100110111010101010000101011011101110110101011100100;
            cmps[7] = uniform < 72'b000000000000000110100001111111111101110001100101101011010110001111011010;
            cmps[8] = uniform < 72'b000000000000000000011111100000001101100010001010011110110110010000101000;
        end else begin
            cmps[0] = uniform < 72'b000000000000000000000001110000111111110110110010000001000000110001101001;
            cmps[1] = uniform < 72'b000000000000000000000000000100101100111100100100110100000011000111111011;
            cmps[2] = uniform < 72'b000000000000000000000000000000001001010010011111100010110000100100011111;
            cmps[3] = uniform < 72'b000000000000000000000000000000000000001101100110010111011010100110011000;
            cmps[4] = uniform < 72'b000000000000000000000000000000000000000000001110101111110110111010111011;
            cmps[5] = uniform < 72'b000000000000000000000000000000000000000000000000001011110101110101111110;
            cmps[6] = uniform < 72'b000000000000000000000000000000000000000000000000000000000111000010011000;
            cmps[7] = uniform < 72'b000000000000000000000000000000000000000000000000000000000000000011000110;
            cmps[8] = uniform < 72'b000000000000000000000000000000000000000000000000000000000000000000000001;
        end
    end

    logic [4:0] sample;
    always_comb begin
        sample = 0;
        foreach (cmps[i])
            sample += cmps[i];
    end

    logic [4:0] sample_store;
    always_ff @(posedge clk) sample_store <= sample;

    assign sample_out = sample + sample_store;
    assign valid = cycle == 1;

endmodule

module base_sampler_rcdt2_reg( // @suppress "File contains multiple design units"
    input logic clk, rst,
    input logic [71:0] uniform,
    output logic [4:0] sample,
    output logic valid
);

    logic [71:0] _uniform;
    logic [4:0] _sample;
    logic _valid;
    base_sampler_rcdt2 inst(.uniform(_uniform),.sample_out(_sample),.clk(clk),.rst(rst),.valid(_valid));

    always_ff @(posedge clk) begin
        _uniform <= uniform;
        sample <= _sample;
        valid <= _valid;
    end
endmodule