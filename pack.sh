#!/bin/bash

set -euo pipefail

# Pack into artifacts zip so that it is under 20MB.

out="$(pwd)/artifacts.zip"

t=$(mktemp -d)
echo "Working in $t"

rsync -av --append-verify --delete --info=progress2 \
    --exclude=.git \
    --exclude=vm/.vagrant \
    --exclude=vm/.env \
    --exclude=vm/vm-vivado.vdi \
    --exclude=vm/vm-root.vmdk \
    --exclude=artifacts.zip \
    --exclude=pack.sh \
    ./ "$t/"

pushd "$t"

BASEURL="https://github.com/mvojacek/ches-2026-falcon-samplerz/tree/main/"

function url() {
    [[ -e "$1" ]] || [[ -f "$1.URL" ]] || { echo "$1 not found!"; return 1; }
    echo "Replacing $1"
    rm -rf "$1"
    cat >"$1.URL" <<EOF
This large file/directory is not included in this archive but can be found at:
${BASEURL}$1
EOF
}

function urls() {
    for f in "$@"; do
        url "$f"
    done
}

urls misc/samplerz_statistics/samples.tar.gz
#urls misc/samplerz_statistics/sampler_fpemu.txt
#urls misc/flopoco_exp_precision/*.gz
#urls misc/samplerz_testvectors/{samplerz-1024.json,test-vector-sampler-falcon1024.txt}
#urls src/registers/doc/fonts
#urls src/registers/sw/py/samplerz_axi/tests
#urls src/sim/data/float_fractional_{,samplerzkat_}testcases.sv
#urls src/sim/histogram_tb_behav.wcfg
#urls out/samplerz.*
#urls sw/out/*
#urls tches2026_4-samplerz.pdf

rm -f "$out"
zip -r "$out" .
du -hs "$out"
