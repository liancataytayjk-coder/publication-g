"""Build the analysis panels (data/processed/panel_q.parquet, panel_a.parquet) and the
administration calendar (output/tables/admin_calendar.csv)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phadmin.calendar import charge_quarters, charge_years  # noqa: E402

PROC, TAB = Path("data/processed"), Path("output/tables")
adm = pd.read_csv("data/manual/administrations.csv", parse_dates=["start_date"])
terms = adm.rename(columns={"admin_id": "label", "start_date": "start"})[["label", "start"]]
ph = pd.read_parquet(PROC / "ph_gdp_q.parquet")
sh = pd.read_parquet(PROC / "shocks_q.parquet")
wdi = pd.read_parquet(PROC / "wdi_a.parquet")
psa_a = pd.read_parquet(PROC / "psa_gdp_a.parquet")


def wdi_series(ind, c):
    s = wdi[(wdi.indicator == ind) & (wdi.country == c)].set_index("year")["value"].sort_index()
    return s.astype(float)


# --- quarterly ----------------------------------------------------------------------------
q = pd.period_range("1981Q1", "2026Q2", freq="Q")
pq = pd.DataFrame(index=q)
pq.index.name = "quarter"
pq["y"] = ph["g"]
pq["y_log"] = ph["g_log"]
pop = wdi_series("population", "PHL")
popg = 100 * np.log(pop).diff()
pq["pop_growth"] = [popg.get(p.year, np.nan) for p in q]
pq["y_pc"] = pq["y"] - pq["pop_growth"]
for lag in [0, 1, 2, 4]:
    pq[f"admin_lag{lag}"] = charge_quarters(terms, q, lag=lag)
pq["admin"] = pq["admin_lag1"]
for c in ["oil_hamilton", "elnino", "oni", "g_us", "g_jp", "g_ea", "ebp"]:
    pq[c] = sh[c].reindex(q)
pq["g_partners"] = pq[["g_us", "g_jp", "g_ea"]].mean(axis=1, skipna=False)
pq.to_parquet(PROC / "panel_q.parquet")
cal = pq["admin"][pq["y"].notna()].dropna()  # quarters with a growth value
cal = cal.groupby(cal, sort=False).agg(first=lambda x: str(x.index.min()), last=lambda x: str(x.index.max()),
                                       quarters="size")
cal.to_csv(TAB / "admin_calendar.csv")

# --- annual -------------------------------------------------------------------------------
years = range(1962, 2026)
qa = pd.period_range("1960Q1", "2025Q4", freq="Q")
lab_q = charge_quarters(terms, qa, lag=1)
lab_q.index = lab_q.index.to_timestamp()
lab_a = charge_years(lab_q)
pa = pd.DataFrame(index=pd.Index(years, name="year"))
pa["admin"] = lab_a.reindex(years)
pa["g_psa"] = psa_a["g"].reindex(years)
pa["g_wb"] = wdi_series("gdp_growth", "PHL").reindex(years)
pa["gpc_wb"] = wdi_series("gdppc_growth", "PHL").reindex(years)
peers = pd.concat({c: wdi_series("gdp_growth", c) for c in ["IDN", "MYS", "THA"]}, axis=1).reindex(years)
pa["g_peers"] = peers.mean(axis=1, skipna=False)
pa["g_rel"] = pa["g_wb"] - pa["g_peers"]
vnm = wdi_series("gdp_growth", "VNM").reindex(years)
pa["g_peers4"] = pd.concat([peers, vnm.rename("VNM")], axis=1).mean(axis=1, skipna=False)
pa["g_rel4"] = pa["g_wb"] - pa["g_peers4"]
pa["inflation"] = wdi_series("cpi_inflation", "PHL").reindex(years)
pa["unemployment"] = wdi_series("unemployment_ilo_modeled", "PHL").reindex(years)
pa.to_parquet(PROC / "panel_a.parquet")
print(cal.to_string())
print(pa.groupby("admin", sort=False).size().to_string())
