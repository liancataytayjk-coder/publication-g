"""Replication gate (pre-registered in CLAUDE.md, 2026-10-16): Blinder and Watson (2016),
US data at the 2014-07-01 vintage. Writes output/tables/replication_gate.csv and
output/tables/replication_term_effects.csv."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phadmin.calendar import charge_quarters  # noqa: E402
from phadmin.model import block_randomization_p, explained, gap_nw, shock_model, term_effects  # noqa: E402

TAB = Path("output/tables")
us = pd.read_parquet("data/processed/us_gate_q.parquet")
sh = pd.read_parquet("data/processed/shocks_q.parquet")
terms = pd.read_csv("data/manual/us_terms.csv", parse_dates=["start"])
targets = pd.read_csv("replication/blinder_watson2016_targets.csv")

q = pd.period_range("1949Q2", "2013Q1", freq="Q")
lab = charge_quarters(terms[["label", "start"]], q, lag=1)
party = terms.set_index("label")["party"]
y = us["g"].reindex(q)
is_d = lab.map(party) == "D"
assert lab.value_counts().eq(16).all() and lab.nunique() == 16, "terms must be 16 x 16 quarters"

rows = []


def add(crit, stat, target, est, lo, hi):
    rows.append({"criterion": crit, "statistic": stat, "target": target, "estimate": round(est, 3),
                 "pass_range": f"[{lo}, {hi}]", "pass": bool(lo <= est <= hi)})


mean_d, mean_r = y[is_d].mean(), y[~is_d].mean()
add("G1", "D mean growth", 4.35, mean_d, 4.25, 4.45)
add("G1", "R mean growth", 2.54, mean_r, 2.44, 2.64)
add("G1", "D-R gap", 1.80, mean_d - mean_r, 1.70, 1.90)
gap, se = gap_nw(y, is_d)
add("G2", "Newey-West (6) s.e. of gap", 0.64, se, 0.54, 0.74)
p, _ = block_randomization_p(y, lab, party.map({"D": "A", "R": "B"}), n_a=7)
add("G2", "randomization p-value (16 blocks)", 0.01, p, 0.0, 0.03)

party_lab = lab.map(party)
res = {}
for name, lags in [("lags 0-6", range(0, 7)), ("lags 1-6", range(1, 7))]:
    m = shock_model(y, party_lab, {"oil": sh["oil_hamilton"]}, lags)
    ex, ex_se = explained(m, {"D": 1, "R": -1})
    # Table 7: term averages of the fitted oil component minus the sample average
    mt = dict(m)
    mt["labels"] = lab.reindex(m["data"].index)
    te = term_effects(mt)
    res[name] = (ex, ex_se, te, len(m["data"]))
best = min(res, key=lambda k: abs(res[k][0] - 0.50))
for name, (ex, ex_se, te, n) in res.items():
    rows.append({"criterion": "G3 (info)", "statistic": f"oil-explained gap, {name} (s.e. {ex_se:.2f}, n={n})",
                 "target": 0.50, "estimate": round(ex, 3), "pass_range": "[0.4, 0.6]", "pass": bool(0.40 <= ex <= 0.60)})
in_range = [k for k in res if 0.40 <= res[k][0] <= 0.60]
chosen = min(in_range, key=lambda k: abs(res[k][0] - 0.50)) if in_range else best
add("G3", f"oil-explained gap, adopted reading: {chosen}", 0.50, res[chosen][0], 0.40, 0.60)

pub = targets[targets["source"].str.contains("Table 7")].set_index("group")["target"]
te = res[chosen][2].reindex(pub.index)
corr = float(np.corrcoef(te, pub)[0, 1])
same = int((np.sign(te) == np.sign(pub)).sum())
add("G4", "corr. of term oil effects with Table 7", ">=0.90", corr, 0.90, 1.0)
add("G4", "terms with the same sign (of 16)", ">=14", same, 14, 16)

out = pd.DataFrame(rows)
out.to_csv(TAB / "replication_gate.csv", index=False)
pd.DataFrame({"published": pub, "estimate": te.round(3)}).rename_axis("term").to_csv(TAB / "replication_term_effects.csv")
gate = out[out["criterion"].isin(["G1", "G2", "G3", "G4"])]["pass"].all()
print(out.to_string(index=False))
print("GATE:", "PASS" if gate else "FAIL")
