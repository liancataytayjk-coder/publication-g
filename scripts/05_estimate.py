"""Estimation, exactly as pre-specified in CLAUDE.md (Estimation plan, 2026-10-16).

Writes to output/tables/: rq1_premiums_q.csv, rq1_premiums_a.csv, rq1_tests.csv,
rq2_single.csv, rq2_joint.csv, rq2_summary.csv, rq3_inheritance.csv,
rq4_same_point.csv, scorecard.csv, robustness.csv, and data/processed/luck_adjusted_q.parquet.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phadmin.model import explained, gap_nw, premiums, shift_test_p, shock_model  # noqa: E402
from phadmin.shocks import purge  # noqa: E402

PROC, TAB = Path("data/processed"), Path("output/tables")
pq = pd.read_parquet(PROC / "panel_q.parquet")
pa = pd.read_parquet(PROC / "panel_a.parquet")
shq = pd.read_parquet(PROC / "shocks_q.parquet")  # full history (1947-), so lags before 1981 exist
shq["g_partners"] = shq[["g_us", "g_jp", "g_ea"]].mean(axis=1, skipna=False)
ORDER = ["macapagal", "marcos_sr", "aquino_c", "ramos", "estrada", "arroyo", "aquino_b", "duterte", "marcos_jr"]
LAGS = range(0, 7)  # D14
SAMPLE = slice(pd.Period("1981Q2"), pd.Period("2026Q2"))


def holm(p):
    p = pd.Series(p).astype(float)
    order = p.sort_values().index
    m, adj, run = len(p), {}, 0.0
    for i, k in enumerate(order):
        run = max(run, min(1.0, (m - i) * p[k]))
        adj[k] = run
    return pd.Series(adj)[p.index]


def premium_table(y, labels):
    """Raw premiums with NW s.e.: P_a = (1 - n_a/n)(mean_a - mean_rest)."""
    d = pd.concat([y.rename("y"), labels.rename("g")], axis=1).dropna()
    base = premiums(d["y"], d["g"])
    n = len(d)
    rows = []
    for a, r in base.iterrows():
        gap, se = gap_nw(d["y"], d["g"] == a)
        k = 1 - r["n"] / n
        z = gap / se
        rows.append({"admin": a, "n": int(r["n"]), "mean": r["mean"], "premium": r["premium"],
                     "check_premium": k * gap, "se": k * se, "p": 2 * (1 - stats.norm.cdf(abs(z)))})
    t = pd.DataFrame(rows).set_index("admin")
    assert np.allclose(t["premium"], t["check_premium"])
    t["p_holm"] = holm(t["p"])
    return t.drop(columns="check_premium").reindex([a for a in ORDER if a in t.index])


def dispersion(t):
    return float(np.sqrt((t["n"] * t["premium"] ** 2).sum() / t["n"].sum()))


def make_shocks(y, foreign="g_us"):
    return {"oil": shq["oil_hamilton"], "us": purge(shq[foreign], y), "elnino": shq["elnino"],
            "ebp": purge(shq["ebp"], y)}


def joint_table(y, labels, shocks, lags=LAGS):
    m = shock_model(y, labels, shocks, lags)
    d, lab = m["data"], m["labels"]
    ybar = d["y"].mean()
    rows = []
    for a in [x for x in ORDER if x in set(lab)]:
        P = d.loc[lab == a, "y"].mean() - ybar
        E, Ese = explained(m, f"premium:{a}")
        row = {"admin": a, "n": int((lab == a).sum()), "premium": P, "explained": E, "explained_se": Ese,
               "unexplained": P - E}
        for k in shocks:
            row[f"explained_{k}"] = explained(m, f"premium:{a}", shock=k)[0]
        rows.append(row)
    t = pd.DataFrame(rows).set_index("admin")
    S = 1 - (t["n"] * t["unexplained"] ** 2).sum() / (t["n"] * t["premium"] ** 2).sum()
    return t, float(S), m


y = pq["y"][SAMPLE]
lab = pq["admin"][SAMPLE]

# ---------------- RQ1 ----------------------------------------------------------------------
t_raw = premium_table(y, lab)
t_pc = premium_table(pq["y_pc"][SAMPLE], lab)
p_shift_raw, _ = shift_test_p(y, lab)
p_shift_pc, _ = shift_test_p(pq["y_pc"][SAMPLE], lab)
q1 = pd.concat({"raw": t_raw, "per_person": t_pc}, names=["measure"]).reset_index()
q1.to_csv(TAB / "rq1_premiums_q.csv", index=False)

ann = {}
tests = [{"test": "shift test, quarterly raw growth 1981Q2-2026Q2", "p": p_shift_raw, "dispersion": dispersion(t_raw)},
         {"test": "shift test, quarterly per-person growth", "p": p_shift_pc, "dispersion": dispersion(t_pc)}]
for col, name in [("g_psa", "annual PSA growth"), ("g_wb", "annual World Bank growth"),
                  ("g_rel", "growth relative to IDN-MYS-THA"), ("g_rel4", "growth relative to IDN-MYS-THA-VNM")]:
    s = pa[col]
    ann[col] = premium_table(s, pa["admin"])
    p, _ = shift_test_p(s.dropna(), pa["admin"][s.notna()])
    tests.append({"test": f"shift test, {name} ({int(s.first_valid_index())}-{int(s.last_valid_index())})",
                  "p": p, "dispersion": dispersion(ann[col])})
pd.concat(ann, names=["measure"]).reset_index().to_csv(TAB / "rq1_premiums_a.csv", index=False)
tests = pd.DataFrame(tests)
disp_ratio = dispersion(ann["g_rel"]) / dispersion(ann["g_psa"])
tests.loc[len(tests)] = {"test": "dispersion ratio: peer-relative / raw annual (H1b if < 0.5)", "p": np.nan,
                         "dispersion": disp_ratio}
tests.to_csv(TAB / "rq1_tests.csv", index=False)

# ---------------- RQ2 ----------------------------------------------------------------------
shocks = make_shocks(y)
single = []
for k, e in shocks.items():
    m = shock_model(y, lab, {k: e}, LAGS)
    d, l = m["data"], m["labels"]
    for a in [x for x in ORDER if x in set(l)]:
        E, se = explained(m, f"premium:{a}")
        single.append({"shock": k, "sample": f"{d.index.min()}-{d.index.max()}", "admin": a,
                       "premium": d.loc[l == a, "y"].mean() - d["y"].mean(), "explained": E, "se": se})
pd.DataFrame(single).to_csv(TAB / "rq2_single.csv", index=False)

t_joint, S, mj = joint_table(y, lab, shocks)
t_joint.to_csv(TAB / "rq2_joint.csv")
fit = mj["fit"]
joint_terms = [c for c in mj["scols"]]
R = np.zeros((len(joint_terms), len(fit.params)))
for i, c in enumerate(joint_terms):
    R[i, list(fit.params.index).index(c)] = 1
wald = fit.wald_test(R, scalar=True)
summary = pd.DataFrame([
    {"item": "joint sample", "value": f"{mj['data'].index.min()}-{mj['data'].index.max()}"},
    {"item": "quarters", "value": len(mj["data"])},
    {"item": "share of premium dispersion explained by luck, S", "value": round(S, 4)},
    {"item": "H2 verdict", "value": "H2b (>0.65)" if S > 0.65 else ("H2a (0.35-0.65)" if S >= 0.35 else "neither (<0.35)")},
    {"item": "Wald test all shock lags = 0, p", "value": float(wald.pvalue)},
    {"item": "R2", "value": round(fit.rsquared, 4)},
])
for k in shocks:
    cols = [c for c in joint_terms if c.startswith(k + "_l")]
    Rk = np.zeros((len(cols), len(fit.params)))
    for i, c in enumerate(cols):
        Rk[i, list(fit.params.index).index(c)] = 1
    summary.loc[len(summary)] = {"item": f"Wald test {k} lags = 0, p", "value": float(fit.wald_test(Rk, scalar=True).pvalue)}
    summary.loc[len(summary)] = {"item": f"sum of {k} lag coefficients", "value": float(fit.params[cols].sum())}
summary.to_csv(TAB / "rq2_summary.csv", index=False)

# luck-adjusted growth: y - (c - mean c) on the joint sample
c = mj["c"]
adj = pd.DataFrame({"y": mj["data"]["y"], "luck": c - c.mean(), "admin": mj["labels"]})
adj["y_adj"] = adj["y"] - adj["luck"]
adj.to_parquet(PROC / "luck_adjusted_q.parquet")

# ---------------- RQ3 ----------------------------------------------------------------------
gdp = pd.read_parquet(PROC / "ph_gdp_q.parquet")["gdp_sa"]
x = 100 * np.log(gdp).diff()
z = 100 * (np.log(gdp.shift(-4)) - np.log(gdp))
Rr = (x < 0).astype(float)
X_ar = pd.concat({f"x_l{j}": x.shift(j) for j in range(5)}, axis=1)
X_nl = pd.concat([X_ar, pd.concat({f"r_l{j}": Rr.shift(j) for j in range(5)}, axis=1),
                  pd.concat({f"rx_l{j}": Rr.shift(j) * x.shift(j) for j in range(5)}, axis=1)], axis=1)
fits = {}
for name, X in [("AR", X_ar), ("bounce-back AR", X_nl)]:
    d = pd.concat([z.rename("z"), X], axis=1).dropna()
    fits[name] = (sm.OLS(d["z"], sm.add_constant(d.drop(columns="z"))).fit(), d)
zbar = fits["AR"][1]["z"].mean()
first = pq["admin"].dropna().groupby(pq["admin"].dropna(), sort=False).apply(lambda s: s.index.min())
rows = []
for a in ["aquino_c", "ramos", "estrada", "arroyo", "aquino_b", "duterte", "marcos_jr"]:
    origin = first[a] - 1
    row = {"admin": a, "first_quarter": str(first[a]), "origin": str(origin),
           "actual": z.get(origin, np.nan), "mean_4q_growth": zbar}
    for name, (f, _) in fits.items():
        xo = sm.add_constant(X_ar if name == "AR" else X_nl, has_constant="add").loc[[origin]]
        row[f"forecast_{name}"] = float(f.predict(xo[f.params.index]).iloc[0])
    row["actual_excess"] = row["actual"] - zbar
    row["forecast_excess_bounce"] = row["forecast_bounce-back AR"] - zbar
    row["H3_inherited"] = bool(row["actual_excess"] > 0 and row["forecast_excess_bounce"] >= 0.5 * row["actual_excess"])
    rows.append(row)
pd.DataFrame(rows).to_csv(TAB / "rq3_inheritance.csv", index=False)

# ---------------- RQ4 ----------------------------------------------------------------------
N = int((lab == "marcos_jr").sum())
rows = []
mj_q = lab[lab == "marcos_jr"].index
for a in [x for x in ORDER if x not in ("macapagal", "marcos_sr")]:
    qa = lab[lab == a].index[:N]
    if len(qa) < N:
        rows.append({"admin": a, "quarters": len(qa), "note": f"fewer than {N} quarters; not compared"})
        continue
    row = {"admin": a, "quarters": N, "first": str(qa[0]), "last": str(qa[-1])}
    for col, src in [("raw", y), ("luck_adjusted", adj["y_adj"])]:
        row[f"{col}_mean"] = src.reindex(qa).mean()
        if a != "marcos_jr":
            s = pd.concat([src.reindex(qa), src.reindex(mj_q)])
            g, se = gap_nw(s.reset_index(drop=True), pd.Series([0] * N + [1] * N))
            row[f"{col}_mj_minus_this"], row[f"{col}_se"] = g, se
    rows.append(row)
pd.DataFrame(rows).to_csv(TAB / "rq4_same_point.csv", index=False)

# ---------------- Objective 1 scorecard -------------------------------------------------------
sc = []
for col in ["g_psa", "gpc_wb", "g_rel", "inflation", "unemployment"]:
    s = pa[col]
    mu, sd = s.mean(), s.std()
    g = pa.groupby("admin")[col].agg(["mean", "count"])
    for a, r in g.iterrows():
        sc.append({"measure": col, "admin": a, "years": int(r["count"]), "mean": r["mean"],
                   "z": (r["mean"] - mu) / sd if r["count"] else np.nan,
                   "period": f"{int(s.first_valid_index())}-{int(s.last_valid_index())}"})
sc = pd.DataFrame(sc)
sc["order"] = sc["admin"].map({a: i for i, a in enumerate(ORDER)})
sc.sort_values(["measure", "order"]).drop(columns="order").to_csv(TAB / "scorecard.csv", index=False)

# ---------------- Robustness -----------------------------------------------------------------
rob = []


def record(spec, yy, ll, sh, lags=LAGS):
    t = premium_table(yy, ll)
    p, _ = shift_test_p(yy.dropna(), ll[yy.notna()])
    tj, Sj, _ = joint_table(yy, ll, sh, lags)
    for a in t.index:
        rob.append({"spec": spec, "admin": a, "premium_raw": t.loc[a, "premium"],
                    "premium_joint": tj["premium"].get(a, np.nan), "explained": tj["explained"].get(a, np.nan),
                    "unexplained": tj["unexplained"].get(a, np.nan), "shift_p": p, "S": Sj})


record("main", y, lab, shocks)
for lag in [0, 2, 4]:
    record(f"timing lag {lag}", y, pq[f"admin_lag{lag}"][SAMPLE], shocks)
ex_covid = y.copy()
ex_covid[pd.period_range("2020Q2", "2021Q1", freq="Q")] = np.nan
record("excluding 2020Q2-2021Q1", ex_covid, lab, shocks)
ex_debt = y.copy()
ex_debt[pd.period_range("1984Q1", "1985Q4", freq="Q")] = np.nan
record("excluding 1984Q1-1985Q4", ex_debt, lab, shocks)
ylog = pq["y_log"][SAMPLE]
record("log growth", ylog, lab, make_shocks(ylog))
record("lags 1-6", y, lab, shocks, lags=range(1, 7))
record("foreign demand US-JP-EA (from 1997)", y, lab, make_shocks(y, foreign="g_partners"))
pd.DataFrame(rob).to_csv(TAB / "robustness.csv", index=False)

print(t_raw.round(3).to_string())
print(tests.round(4).to_string())
print(t_joint.round(3).to_string())
print(summary.to_string())
