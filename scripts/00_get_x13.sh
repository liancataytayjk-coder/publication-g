#!/usr/bin/env bash
# Fetch the US Census Bureau's X-13ARIMA-SEATS binary (v1.1 build 61) into .tools/ (not committed).
set -euo pipefail
D=.tools/x13
[ -x "$D/x13as/x13as" ] && { echo "x13as present"; exit 0; }
mkdir -p "$D"
curl -sS -m 300 -o "$D/x13as.tar.gz" \
  https://www2.census.gov/software/x-13arima-seats/x13as/unix-linux/program-archives/x13as_ascii-v1-1-b61.tar.gz
tar xzf "$D/x13as.tar.gz" -C "$D"
ln -sf x13as_ascii "$D/x13as/x13as"
echo "x13as installed in $D/x13as"
