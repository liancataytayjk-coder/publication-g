"""Download FRED and ALFRED series unchanged.

US real GDP at the reference paper's data vintage (ALFRED, 2014-07-01) for the
replication gate; current-vintage US real GDP (foreign demand); PPI crude
petroleum (Hamilton oil shock); crude oil prices in dollars (robustness);
Japanese and euro-area real GDP (trading-partner composite from the 1990s).
"""
from _raw import fetch

FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
ALFRED = "https://alfred.stlouisfed.org/graph/alfredgraph.csv?id={}&vintage_date={}"

fetch(ALFRED.format("GDPC1", "2014-07-01"), "data/raw/fred/gdpc1_vintage20140701.csv.gz")
for sid in ["GDPC1", "WPU0561", "MCOILWTICO", "POILDUBUSDM", "POILBREUSDQ",
            "JPNRGDPEXP", "CLVMNACSCAB1GQEA19", "USREC"]:
    fetch(FRED.format(sid), f"data/raw/fred/{sid.lower()}.csv.gz")
