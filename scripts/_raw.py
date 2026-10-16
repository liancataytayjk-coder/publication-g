"""Save a URL's response unchanged, gzipped, under data/raw/ (skip if present unless --force)."""
import gzip
import sys
import time
from pathlib import Path

import requests

FORCE = "--force" in sys.argv


def fetch(url, out, headers=None):
    out = Path(out)
    if out.exists() and not FORCE:
        print("exists:", out)
        return out
    for attempt in range(5):
        try:
            r = requests.get(url, timeout=120, headers=headers or {"User-Agent": "curl/8.5.0"})  # ALFRED drops unknown agents
            r.raise_for_status()
            break
        except requests.RequestException:
            if attempt == 4:
                raise
            time.sleep(2 ** (attempt + 1))
    out.parent.mkdir(parents=True, exist_ok=True)
    with gzip.GzipFile(out, "wb", mtime=0) as f:
        f.write(r.content)
    print(f"wrote {out}: {len(r.content)} bytes")
    return out
