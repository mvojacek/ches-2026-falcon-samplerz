#!/bin/bash

# Packages files for CHES artifacts submission (20MB), large data is replaced with a GitHub link

set -euo pipefail

cd "$(dirname "$(realpath "$0")")"
out="$(pwd)/artifacts.zip"
t=$(mktemp -d)
trap 'rm -rf "$t"' EXIT
mkdir "$t/package"

rsync -a --safe-links --from0 \
    --files-from=<(git ls-files --cached --others --exclude-standard -z) \
    --exclude=/pack.sh \
    ./ "$t/package/"

cd "$t/package"
BASEURL="https://github.com/mvojacek/ches-2026-falcon-samplerz/tree/main/"

function url() {
    [[ -e "$1" ]] || [[ -f "$1.URL" ]] || { echo "$1 not found!" >&2; return 1; }
    rm -rf "$1"
    printf 'This large file/directory is not included in this archive but can be found at:\n%s%s\n' "$BASEURL" "$1" >"$1.URL"
}


url misc/samplerz_statistics/samples.tar.xz

zip -qr "$t/artifacts.zip" .
if (( $(stat -c %s "$t/artifacts.zip") > 20000000 )); then
    echo "Package exceeds 20 MB" >&2
    exit 1
fi
mv "$t/artifacts.zip" "$out"
du -hs "$out"
