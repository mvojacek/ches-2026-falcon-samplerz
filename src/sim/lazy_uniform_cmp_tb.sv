`timescale 1ns/1ps

module lazy_uniform_cmp_tb;

    localparam W = 10;
    localparam W_BITS = $clog2(W);
    logic [W-1:0] in, uniform;
    logic in_gt, in_lt, eq;
    logic [W_BITS-1:0] used_bits;
    
    lazy_uniform_cmp #(.W(W)) dut (
        .in(in),
        .uniform(uniform),
        .in_gt(in_gt), .in_lt(in_lt), .eq(eq),
        .used_bits(used_bits)
    );

    function int calculate_used_bits(input logic [W-1:0] in, input logic [W-1:0] uniform);
        for (int i = 1; i <= W; i++) begin
            if (in[W-i] != uniform[W-i]) begin
                return i;
            end
        end
        return W;
        
    endfunction
    

    int calc_used_bits;
    logic [W-1:0] used_bits_mask;
    initial begin
        for (int i = 0; i < 2**W; i++) begin
            in = i;
            for (int j = 0; j < 2**W; j++) begin
                uniform = j;
                #1;
                calc_used_bits = calculate_used_bits(in, uniform);
                used_bits_mask = (1 << (W - calc_used_bits)) - 1;
                if (in_gt !== (in > uniform) || in_lt !== (in < uniform) || eq !== (in == uniform) || used_bits !== calc_used_bits) begin
                    $display("Mismatch:\n| in   = %b\n| uni  = %b\n| mask = %b\n| in_gt = %b, in_lt = %b, eq = %b\n| used_bits = %0d, calc_used_bits = %0d",
                        in, uniform, used_bits_mask,
                        in_gt, in_lt, eq,
                        used_bits, calc_used_bits);
                end
            end
        end
        $display("All done!");
    end
    
endmodule

