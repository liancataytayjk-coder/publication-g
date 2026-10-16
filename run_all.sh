#!/usr/bin/env bash
# Rebuild everything from data/raw/. Use --download to refresh the raw data first.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PY:-.venv/bin/python}
if [[ "${1:-}" == "--download" ]]; then
  for s in psa fred worldbank other; do $PY scripts/01_download_$s.py --force; done
fi
bash scripts/00_get_x13.sh
$PY -m pytest -q
$PY scripts/02_clean.py
$PY scripts/04_replicate.py
for s in scripts/05_*.py scripts/06_*.py scripts/07_*.py scripts/08_*.py; do
  [ -e "$s" ] && $PY "$s"
done
echo "done"
