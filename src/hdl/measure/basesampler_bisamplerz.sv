// from: https://github.com/Shaibk/Bi-SamplerZ, modified
// licensed under: http://www.apache.org/licenses/LICENSE-2.0

module basesampler_bisamplerz (
    input logic [71:0] rdm72,
    output logic [4:0] z0
);

localparam logic [71:0] RCDT [0:17] = '{72'd3024686241123004913666,72'd1564742784480091954050,72'd636254429462080897535,72'd199560484645026482916,72'd47667343854657281903,
72'd859590200636044063,72'd116329795344668388,72'd117656387352093658,72'd8867391802663976,72'd496969357462633,72'd20680885154299,72'd638331848991,72'd14602316184,72'd247426747,72'd3104126,72'd28824,72'd198,72'd1};

logic cmp[18:0];
logic sel [18:0];
tri [4:0] z;

//Generate comparison result 
always_comb begin
    for (int i = 0; i < 18; i++) begin
        cmp[i] = (rdm72 < RCDT[i]);
    end
    cmp[18] = 'b0; //Last element is always 1
end

//Generate 'NAND' logic
always_comb begin 
    sel[0] = ~cmp[0];
    for (int j = 0; j < 18; j++)begin
        sel[j+1] = cmp[j] & (~cmp[j+1]);
    end
end
//Generate tri-state net
genvar k;
generate 
    for (k = 0; k < (18 +1); k++) begin : tri_driver
        assign z = sel[k]? k : 'bz;
    end
endgenerate
//Generate z0 siganl
assign z0 = z;
endmodule

module basesampler_bisamplerz_reg (
    input logic clk,
    input logic [71:0] rdm72,
    output logic [4:0] z0
);

logic [71:0] _rdm72;
logic [4:0] _z0;
always_ff @(posedge clk) begin
    _rdm72 <= rdm72;
    z0 <= _z0;
end

basesampler_bisamplerz inst (
    .rdm72(_rdm72),
    .z0(_z0)
);

endmodule
