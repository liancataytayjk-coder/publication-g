"""Assemble the replication package for deposit (Zenodo) as deliverables/<name>.zip.

Contents: code (phadmin/, scripts/, tests/, run_all.sh, requirements.txt), raw data
(data/raw/, with its source log), hand-entered tables (data/manual/), the
reference targets (replication/), all outputs (output/), the article and annex
(paper/, docs/), a README_REPLICATION.md written here, .zenodo.json and
CITATION.cff. Processed data are not included: run_all.sh rebuilds them.
"""
import datetime as dt
import json
import platform
import shutil
import subprocess
import sys
import zipfile
from importlib import metadata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "phl-presidents-growth-replication"
OUT = ROOT / "deliverables"
INCLUDE = ["phadmin", "scripts", "tests", "data/raw", "data/manual", "replication", "output", "paper", "docs",
           "run_all.sh", "requirements.txt", "pytest.ini", "README.md", ".zenodo.json", "CITATION.cff"]
SKIP = {"__pycache__", ".pytest_cache", "session_handoff.Rmd"}
n = json.loads((ROOT / "output/tables/paper_numbers.json").read_text())


def version(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout.strip().splitlines()[0]
    except Exception:  # noqa: BLE001
        return "not available"


pkgs = [l.split("=")[0].split(">")[0].strip() for l in (ROOT / "requirements.txt").read_text().split() if l.strip()]
vers = []
for p in pkgs:
    try:
        vers.append(f"{p} {metadata.version(p)}")
    except metadata.PackageNotFoundError:
        vers.append(f"{p} (not installed)")

try:
    import pypandoc
    pandoc_version = pypandoc.get_pandoc_version()
except Exception:  # noqa: BLE001
    pandoc_version = "not available"
readme = f"""# Replication package

**Article.** Lian Cataytay, "Good policy or good luck? Philippine economic performance
across presidential administrations." Manuscript submitted to the *Asian Economic
Journal*. Draft of {n['build_date']}.

**Contact.** Lian Cataytay, University of Southeastern Philippines,
lrcataytay00745@usep.edu.ph.

## What this package does

One command rebuilds every number, table and figure in the article from the raw
data files, and renders the article and its statistical annex:

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements_lock.txt   # exact versions used
./run_all.sh              # about 3 minutes; add --download to re-download the raw data
```

`run_all.sh` (1) fetches the US Census Bureau's X-13ARIMA-SEATS program (v1.1 build
61) into `.tools/`, (2) runs the simulation tests of the estimator, (3) cleans the
raw data and seasonally adjusts Philippine GDP, (4) builds the quarterly and
annual panels, (5) runs the replication of Blinder and Watson (2016) on US data,
which must pass before any Philippine estimate is used, (6) estimates every
model, (7) draws the figures and (8) renders `paper/manuscript.docx` and
`docs/statistical_annex.docx` (and PDF copies, if LibreOffice is installed),
then checks their layout.

## Check that it worked

`output/tables/replication_gate.csv` must show `pass = True` for every criterion
(D–R gap {n['gate_gap']} against 1.80 in the original). The headline Philippine
numbers are in `output/tables/paper_numbers.json`; for example, the Aquino III
premium is {n['p_aquino_b']} points and the share of the spread of premiums
explained by luck is {n['S']}. Reruns reproduce the tables and figures exactly.

## File map

| Folder or file | Contents |
|---|---|
| `data/raw/` | Untouched downloads (gzipped); `data/raw/source_log.md` gives the URL, date pulled, units and coverage of each file |
| `data/manual/` | Presidents' term dates (Philippines, United States), typed from cited sources |
| `replication/` | The reference paper's published numbers that the replication must match |
| `phadmin/` | The estimator: quarter-to-administration calendar, shocks, premiums, randomization tests |
| `tests/` | Simulation and unit tests (`pytest`) |
| `scripts/01_download_*.py` | Download scripts (used only with `--download`) |
| `scripts/02_clean.py` … `06_figures.py` | Cleaning, panels, replication gate, estimation, figures |
| `scripts/08_paper.py` | Builds `output/tables/paper_numbers.json` and renders the article from `paper/manuscript_template.md` |
| `scripts/style/`, `paper/style/` | Document layout (template, finishing script, checker) |
| `output/tables/`, `output/figures/` | Every estimate (csv) and figure (PNG, TIFF, PDF) |
| `paper/`, `docs/` | The article, statistical annex and their templates; `paper/references.bib` |

## Software used

Python {platform.python_version()} on {platform.system()}; {', '.join(vers)}.
pandoc {pandoc_version} (bundled with pypandoc_binary). X-13ARIMA-SEATS
v1.1 build 61. {version(['soffice', '--version'])} (PDF copies only). Fonts: Times
New Roman (Liberation Serif, same metrics, where Times is not installed).

## Data sources and terms of use

All data are public. They are redistributed here only so that the results can be
reproduced, each under its provider's terms; cite the providers when reusing
them. Philippine Statistics Authority (OpenSTAT national accounts); World Bank,
World Development Indicators (CC BY 4.0); US Bureau of Economic Analysis and
Bureau of Labor Statistics series via FRED and ALFRED (Federal Reserve Bank of St.
Louis); Japanese and euro-area GDP via FRED (original providers' terms apply);
NOAA Climate Prediction Center (Oceanic Niño Index); Board of Governors of the
Federal Reserve System (excess bond premium); IMF International Financial
Statistics via DBnomics (cross-check only); Wikipedia, "List of presidents of the
Philippines" (CC BY-SA 4.0; source of term dates). The full list, with URLs and
dates, is in `data/raw/source_log.md`.

## Not included

The reference paper (Blinder and Watson 2014, NBER Working Paper 20324; 2016,
*American Economic Review*), for copyright; the X-13 program, which `run_all.sh`
downloads from the US Census Bureau; processed data, which `run_all.sh` rebuilds.
"""

zen = {
    "title": "Replication package for: Good policy or good luck? Philippine economic performance "
             "across presidential administrations",
    "upload_type": "software",
    "description": "Code, raw data and outputs that reproduce every number, table and figure in the article, "
                   "including a replication of Blinder and Watson (2016) on US data. Run ./run_all.sh.",
    "creators": [{"name": "Cataytay, Lian", "affiliation": "University of Southeastern Philippines"}],
    "keywords": ["Philippines", "presidents", "economic growth", "luck", "replication"],
    "related_identifiers": [{"identifier": "10.1257/aer.20140913", "relation": "isSupplementTo",
                             "scheme": "doi", "resource_type": "publication-article"}],
    "license": "cc-by-4.0",
}
cff = f"""cff-version: 1.2.0
message: "If you use this package, please cite it as below."
title: "Replication package for: Good policy or good luck? Philippine economic performance across presidential administrations"
authors:
  - family-names: Cataytay
    given-names: Lian
    affiliation: University of Southeastern Philippines
    email: lrcataytay00745@usep.edu.ph
date-released: {dt.date.today().isoformat()}
type: software
"""

if __name__ == "__main__":
    (ROOT / ".zenodo.json").write_text(json.dumps(zen, indent=2) + "\n")
    (ROOT / "CITATION.cff").write_text(cff)
    stage = OUT / NAME
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    (stage / "README_REPLICATION.md").write_text(readme)
    lock = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True).stdout
    (stage / "requirements_lock.txt").write_text(lock)
    for item in INCLUDE:
        src = ROOT / item
        if src.is_dir():
            shutil.copytree(src, stage / item, ignore=shutil.ignore_patterns(*SKIP))
        elif src.exists():
            (stage / item).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, stage / item)
    zpath = OUT / f"{NAME}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(stage.rglob("*")):
            if f.is_file():
                z.write(f, Path(NAME) / f.relative_to(stage))
    print(f"wrote {zpath} ({zpath.stat().st_size / 1e6:.1f} MB, {sum(1 for _ in stage.rglob('*') if _.is_file())} files)")
    sys.exit(0)
