
module prng_refill #(
    parameter REFILL_W = 8,
    parameter REFILL_PORTS = 3
)(
    input logic clk, rst,

    input logic [32*11-1:0] seed,
    input logic [63:0] counter,
    output logic counter_use,

    refill_if.source refill [REFILL_PORTS]
);

    logic [255:0] key;
    logic [63:0] iv;
    assign key = seed[0+:256];
    assign iv = seed[256+:64];

`ifdef DEV_URANDOM
    genvar i;
    generate
        for (i = 0; i < REFILL_PORTS; i = i + 1) begin : block
            file_refill #(
                .FILE("/dev/urandom")
            ) file_refill_instance (
                .clk(clk),
                .refill(refill[i])
            );
        end
    endgenerate

    assign counter_use = 1'b0;
`else

    logic chacha_init, chacha_valid;
    logic [511:0] chacha_out;
    `ifdef SZ_KEEP_HIERARCHY
    (* keep_hierarchy = "yes" *)
`endif
    chacha_core chacha_inst (
        .clk(clk),
        .reset_n(~rst),
        .init(chacha_init),
        .next('0),
        .key(key),
        .keylen('b1),
        .iv(iv),
        .ctr(counter),
        .rounds('d20),
        .data_in('0),
        .ready(),
        .data_out(chacha_out),
        .data_out_valid(chacha_valid)
    );

    assign counter_use = chacha_init; // increment counter if the value is used

    typedef enum {
        START,
        WAITING,
        DONE
    } state_t;

    state_t state, next_state;
    always_ff @(posedge clk) begin
        if (!rst) begin
            state <= START;
        end else begin
            state <= next_state;
        end
    end

    // run the cha cha core continuously
    always_comb begin
        chacha_init = 1'b0;
        next_state = state;
        case (state)
            START: begin
                chacha_init = 1'b1;
                next_state = WAITING;
            end
            WAITING: begin
                if (chacha_valid) begin
                    next_state = DONE;
                end
            end
            DONE: begin
                next_state = START;
            end
            default: begin
                next_state = START;
            end
        endcase
    end

    // buffer the random block until it is used
    logic [511:0] random_buf;
    logic random_buf_valid, random_buf_used;
    always_ff @(posedge clk) begin
        if (rst) begin
            random_buf <= 'X;
            random_buf_valid <= 1'b0;
        end else if (chacha_valid) begin
            random_buf <= chacha_out;
            random_buf_valid <= 1'b1;
        end else if (random_buf_used) begin
            random_buf_valid <= 1'b0;
        end
    end

    // split the random block into REFILL_W bit parts
    localparam int BITS_PER_REFILL = 512 / REFILL_PORTS;
    // determine number of words per refill
    localparam int REFILL_WORDS = BITS_PER_REFILL / REFILL_W;
    localparam int REFILL_WORDS_BITS = $clog2(REFILL_WORDS);

    logic do_refill;
    logic [REFILL_PORTS-1:0] needs_refill;
    genvar j;
    generate
        for (j = 0; j < REFILL_PORTS; j = j + 1) begin : refill_block
            logic [REFILL_W-1:0] refill_data [REFILL_WORDS-1:0];
            logic [REFILL_WORDS_BITS-1:0] refill_count;

            assign needs_refill[j] = refill_count == 0 || (refill_count == 1 && refill[j].refill_req);

            assign refill[j].refill_valid = refill_count != 0;
            assign refill[j].refill = refill_data[refill_count-1];

            always_ff @(posedge clk) begin
                if (rst) begin
                    refill_count <= '0;
                    refill_data <= '{default: 'X};
                end else begin
                    if (refill[j].refill_req && refill_count != 0) begin
                        refill_count <= refill_count - 1;
                    end

                    if (do_refill) begin
                        refill_count <= REFILL_WORDS;
                        {<<{refill_data}} <= random_buf[j*BITS_PER_REFILL+:BITS_PER_REFILL];
                    end
                end
            end
        end
    endgenerate

    always_comb begin
        do_refill = random_buf_valid && |needs_refill;
        random_buf_used = do_refill;
    end

`endif

endmodule
