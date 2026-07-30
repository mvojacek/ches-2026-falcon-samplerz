`timescale 1ns/1ps

module delay #(
    type delay_t = logic,
    parameter STAGES = 5
)(
    input clk,
    input delay_t in,
    output delay_t out
);
    generate
        if (STAGES == 0) begin
            assign out = in;
        end else begin
            delay_t shiftreg [0:STAGES-1];

            always_ff @(posedge clk) begin
                shiftreg[0] <= in;
                for (int i = 0; i < STAGES-1; i++) begin
                    shiftreg[i+1] <= shiftreg[i];
                end
            end

            assign out = shiftreg[STAGES-1];
        end
    endgenerate
endmodule
