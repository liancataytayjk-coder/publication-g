"""Download PSA OpenSTAT national accounts tables unchanged (constant 2018 prices).

Quarterly GDP by expenditure: the long series (Q1 1981 onward), the current
table (2000 onward, latest quarter), PSA's seasonally adjusted table (2000
onward); annual GDP 1946 onward; annual per-capita GDP. Each file is logged in
data/raw/source_log.md.
"""
import subprocess
import sys
from pathlib import Path

API = "https://openstat.psa.gov.ph/PXWeb/api/v1/en/DB/2B/"
TABLES = [
    ("NA/QT/23QNAP/EXP/0952B5BQEQ1.px", "gdp_q_byexpenditure_1981_latest.csv.gz"),
    ("NA/QT/1SUM/0012B5BEXQ1.px", "gni_gdp_q_byexpenditure_2000_latest.csv.gz"),
    ("SANA/1SUM/012B5BEXS1.px", "gni_gdp_q_sa_byexpenditure_2000_latest.csv.gz"),
    ("NA/AN/23ANAP/0942B5BANA1.px", "gdp_a_byindustry_1946_latest.csv.gz"),
    ("NA/AN/1SUM/0122B5BPCA1.px", "percapita_gdp_gni_hfce_a.csv.gz"),
]

here = Path(__file__).parent
for table, name in TABLES:
    cmd = [sys.executable, str(here / "pxweb_download.py"), API, table, f"data/raw/psa/{name}"]
    subprocess.run(cmd + sys.argv[1:], check=True)  # e.g. --force
