#!/bin/bash

set -euo pipefail
set -x

INPUT=$1
FILE=$2
USED=1 # set to 0 to force used output to 0 - results in less LUTs

tail -n+5 "$INPUT" | sort > "$INPUT".noheader
INPUT=$INPUT.noheader

bits=$(awk 'NF==2{print length($1); exit}' "$INPUT")

cat >"$FILE" <<EOF
\`timescale 1ns / 1ps
module base_sampler_pla_smart(
    input logic [$((bits-1)):0] uniform,
    output logic [4:0] sample,
    output logic [6:0] used
);

always_comb begin
    casez (uniform)
EOF

cat "$INPUT" | tr '-' '?' | awk "NF==2{s = \$1; z=gsub(/0/, \"\", s); o=gsub(/1/, \"\", s); print \"        $bits'b\" \$1 \": begin sample <= 5'b\" \$2 \"; used = \" (z+o) \"; end\"}" >> "$FILE"

if [[ $USED != 1 ]]; then
	echo "        used = 0;" >> "$FILE"
fi

cat >>"$FILE" <<EOF
    endcase
end
endmodule
EOF
