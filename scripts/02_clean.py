"""Clean raw files into tidy processed tables (data/processed/, parquet).

Outputs
- ph_gdp_q.parquet: PSA real GDP (constant 2018 prices) NSA, our X-13 seasonally adjusted
  series, PSA's own SA series; growth at a compounded annual rate (D13; 400*dln kept as g_log) and 100*dln over 4 quarters.
- shocks_q.parquet: quarterly shock inputs (PPI crude, Hamilton measure, US/JP/EA growth,
  ONI positive part, excess bond premium).
- us_gate_q.parquet: US real GDP growth at the 2014-07-01 vintage.
- wdi_a.parquet: World Bank annual indicators, long format.
- psa_gdp_a.parquet: PSA annual real GDP 1946-.
Also writes output/tables/sa_check.csv (decision D10 check).
"""
import gzip
import json
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.tsa.x13 import x13_arima_analysis

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phadmin.shocks import hamilton_net_increase, monthly_to_quarterly


def ann(x):
    """Quarterly growth at a compounded annual rate, 100*((x_t/x_{t-1})^4 - 1): the
    reference paper's definition (decision D13)."""
    return 100 * ((x / x.shift(1)) ** 4 - 1)

RAW, PROC, TAB = Path("data/raw"), Path("data/processed"), Path("output/tables")
PROC.mkdir(parents=True, exist_ok=True)
TAB.mkdir(parents=True, exist_ok=True)
X13 = ".tools/x13/x13as"


def psa_row(fname, row, prefix):
    d = pd.read_csv(RAW / "psa" / fname, dtype=str)
    s = d.set_index(d.columns[0]).loc[row]
    s = s[[c for c in s.index if c.startswith(prefix)]]
    lab = [c[len(prefix):].strip() for c in s.index]
    return pd.to_numeric(pd.Series(s.values, index=lab), errors="coerce").dropna()


def fred(name, col=None):
    d = pd.read_csv(RAW / "fred" / f"{name}.csv.gz")
    s = pd.to_numeric(d.iloc[:, 1], errors="coerce")
    s.index = pd.to_datetime(d.iloc[:, 0])
    return s.dropna()


def to_q(s):
    s = s.copy()
    s.index = pd.PeriodIndex(s.index, freq="Q")
    return s


# --- Philippine quarterly GDP -------------------------------------------------------------
nsa = psa_row("gdp_q_byexpenditure_1981_latest.csv.gz", "Gross Domestic Product", "At Constant 2018 Prices")
nsa.index = pd.PeriodIndex([i.replace(" ", "") for i in nsa.index], freq="Q")
cur = psa_row("gni_gdp_q_byexpenditure_2000_latest.csv.gz", "..Gross Domestic Product", "At Constant 2018 Prices")
cur.index = pd.PeriodIndex([i.replace(" ", "") for i in cur.index], freq="Q")
ov = nsa.index.intersection(cur.index)
assert np.allclose(nsa[ov], cur[ov]), "long series and current table disagree"
psa_sa = psa_row("gni_gdp_q_sa_byexpenditure_2000_latest.csv.gz", "..Gross Domestic Product", "")
psa_sa.index = pd.PeriodIndex([i.replace(" ", "") for i in psa_sa.index], freq="Q")

ts = nsa.copy()
ts.index = ts.index.to_timestamp()
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    x = x13_arima_analysis(ts, x12path=X13, log=True, outlier=True, trading=False)
sa = to_q(x.seasadj)
ph = pd.DataFrame({"gdp_nsa": nsa, "gdp_sa": sa, "gdp_sa_psa": psa_sa})
ph["g"] = ann(ph["gdp_sa"])
ph["g_log"] = 400 * np.log(ph["gdp_sa"]).diff()
ph["g_psa_sa"] = ann(ph["gdp_sa_psa"])
ph["g_yoy"] = 100 * np.log(ph["gdp_nsa"]).diff(4)
ph.index.name = "quarter"
ph.to_parquet(PROC / "ph_gdp_q.parquet")
o = ph[["g", "g_psa_sa"]].dropna()
pd.DataFrame([{"check": "corr of q/q SA growth, ours vs PSA", "sample": f"{o.index.min()}-{o.index.max()}",
               "n": len(o), "value": round(o["g"].corr(o["g_psa_sa"]), 4), "pass_rule": ">= 0.90",
               "pass": bool(o["g"].corr(o["g_psa_sa"]) >= 0.90)}]).to_csv(TAB / "sa_check.csv", index=False)

# --- Shocks (quarterly) -------------------------------------------------------------------
ppi = monthly_to_quarterly(fred("wpu0561"))
sh = pd.DataFrame({"ppi_crude": ppi, "oil_hamilton": hamilton_net_increase(ppi)})
sh["g_us"] = ann(to_q(fred("gdpc1")))
sh["g_jp"] = ann(to_q(fred("jpnrgdpexp")))
sh["g_ea"] = ann(to_q(fred("clvmnacscab1gqea19")))
oni = pd.read_csv(RAW / "noaa" / "oni_ascii.txt.gz", sep=r"\s+")
season_mid = {"DJF": 1, "JFM": 2, "FMA": 3, "MAM": 4, "AMJ": 5, "MJJ": 6, "JJA": 7, "JAS": 8,
              "ASO": 9, "SON": 10, "OND": 11, "NDJ": 12}  # centre month of each 3-month season
oni["date"] = pd.to_datetime(dict(year=oni["YR"], month=oni["SEAS"].map(season_mid), day=1))
oni_m = pd.Series(oni["ANOM"].values, index=oni["date"])
sh["oni"] = monthly_to_quarterly(oni_m)
sh["elnino"] = monthly_to_quarterly(oni_m.clip(lower=0))
ebp = pd.read_csv(RAW / "frb" / "ebp_monthly.csv.gz", parse_dates=["date"]).set_index("date")["ebp"]
sh["ebp"] = monthly_to_quarterly(ebp)
sh.index.name = "quarter"
sh.to_parquet(PROC / "shocks_q.parquet")

# --- US gate data -------------------------------------------------------------------------
us = to_q(fred("gdpc1_vintage20140701"))
pd.DataFrame({"gdp": us, "g": ann(us), "g_log": 400 * np.log(us).diff()}).rename_axis("quarter").to_parquet(PROC / "us_gate_q.parquet")

# --- World Bank annual --------------------------------------------------------------------
rows = []
for f in sorted((RAW / "worldbank").glob("wdi_*_5countries.json.gz")):
    name = f.name[len("wdi_"):-len("_5countries.json.gz")]
    for r in json.load(gzip.open(f))[1]:
        rows.append((name, r["countryiso3code"], int(r["date"]), r["value"]))
wdi = pd.DataFrame(rows, columns=["indicator", "country", "year", "value"]).dropna()
wdi.to_parquet(PROC / "wdi_a.parquet")

# --- PSA annual GDP -----------------------------------------------------------------------
ga = psa_row("gdp_a_byindustry_1946_latest.csv.gz", "Gross Domestic Product", "At Constant 2018 Prices")
ga.index = ga.index.astype(int)
pd.DataFrame({"gdp_real": ga, "g": 100 * np.log(ga).diff()}).rename_axis("year").to_parquet(PROC / "psa_gdp_a.parquet")

print("PH GDP", ph.index.min(), ph.index.max(), "| SA check corr", round(o["g"].corr(o["g_psa_sa"]), 4))
print("shocks", {c: (str(sh[c].first_valid_index()), str(sh[c].last_valid_index())) for c in sh})
print("US vintage", us.index.min(), us.index.max())
