"""Build the numbers dictionary n and tables t from output/tables, then render the
manuscript and the statistical annex from their templates.

No estimate is typed by hand: every number in the documents comes from n
(saved to output/tables/paper_numbers.json) or from a table in t. Verdicts are
computed here from the numbers with the rules pre-registered in CLAUDE.md.
"""
import datetime as dt
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_doc import render  # noqa: E402

TAB = Path("output/tables")
ADM = pd.read_csv("data/manual/administrations.csv").set_index("admin_id")
NAME = ADM["short"].to_dict()
ORDER = ["macapagal", "marcos_sr", "aquino_c", "ramos", "estrada", "arroyo", "aquino_b", "duterte", "marcos_jr"]
f2 = lambda x: f"{x:.2f}"  # noqa: E731
sgn = lambda x: f"{x:+.2f}"  # noqa: E731


def p_fmt(p):
    return "< 0.001" if p < 0.001 else f"{p:.3f}" if p < 0.01 else f"{p:.2f}"


def stars(p):
    return "" if pd.isna(p) else "\\*\\*\\*" if p < 0.01 else "\\*\\*" if p < 0.05 else "\\*" if p < 0.10 else ""


def md_table(df, caption, note=None):
    cols = list(df.columns)
    out = ["", f"**{caption}**", "", "| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    out += ["| " + " | ".join(str(v) for v in r) + " |" for r in df.itertuples(index=False)]
    out.append("")
    if note:
        out += [f"*Note.* {note}", ""]
    return "\n".join(out)


def build():
    n, t = {"build_date": dt.date.today().strftime("%d %B %Y")}, {}

    # ---- sample, data checks ---------------------------------------------------------------
    cal = pd.read_csv(TAB / "admin_calendar.csv").set_index("admin")
    q1 = pd.read_csv(TAB / "rq1_premiums_q.csv")
    raw = q1[q1.measure == "raw"].set_index("admin")
    pc = q1[q1.measure == "per_person"].set_index("admin")
    n["n_q"] = int(raw["n"].sum())
    n["mean_q"] = f2((raw["n"] * raw["mean"]).sum() / raw["n"].sum())
    n["sa_corr"] = f"{pd.read_csv(TAB / 'sa_check.csv')['value'].iloc[0]:.3f}"
    n["mj_quarters"] = int(cal.loc["marcos_jr", "quarters"])
    n["mj_last"] = cal.loc["marcos_jr", "last"]

    # ---- replication gate --------------------------------------------------------------------
    g = pd.read_csv(TAB / "replication_gate.csv")
    gv = lambda s: float(g.loc[g.statistic.str.startswith(s), "estimate"].iloc[0])  # noqa: E731
    n.update(gate_d=f2(gv("D mean")), gate_r=f2(gv("R mean")), gate_gap=f2(gv("D-R gap")),
             gate_se=f2(gv("Newey-West")), gate_p=f"{gv('randomization'):.3f}",
             gate_oil=f2(gv("oil-explained gap, adopted")), gate_corr=f"{gv('corr.'):.3f}",
             gate_signs=int(gv("terms with")))
    gt = g[g.criterion.isin(["G1", "G2", "G3", "G4"])].copy()
    gt["pass"] = gt["pass"].map({True: "yes", False: "no"})
    t["gate"] = md_table(gt.rename(columns={"criterion": "Criterion", "statistic": "Statistic", "target": "Paper",
                                            "estimate": "This study", "pass_range": "Pass range", "pass": "Pass"}),
                         "Table 1. Replication of Blinder and Watson (2016) on US data, 1949Q2–2013Q1",
                         "Pass ranges were fixed before the gate was run. Growth is quarterly real GDP growth at a "
                         "compounded annual rate, ALFRED vintage of 1 July 2014.")

    # ---- RQ1 -------------------------------------------------------------------------------
    for a, r in raw.iterrows():
        n[f"p_{a}"], n[f"p_{a}_se"], n[f"p_{a}_p"], n[f"p_{a}_holm"] = sgn(r.premium), f2(r.se), p_fmt(r.p), p_fmt(r.p_holm)
    for a, r in pc.iterrows():
        n[f"pc_{a}"], n[f"pc_{a}_se"], n[f"pc_{a}_p"], n[f"pc_{a}_holm"] = sgn(r.premium), f2(r.se), p_fmt(r.p), p_fmt(r.p_holm)
    rows = []
    for a in [x for x in ORDER if x in raw.index]:
        lab = NAME[a] + (" (1981–86)" if a == "marcos_sr" else "")
        rows.append([lab, f"{cal.loc[a, 'first']}–{cal.loc[a, 'last']}", int(raw.loc[a, "n"]), f2(raw.loc[a, "mean"]),
                     f"{sgn(raw.loc[a, 'premium'])}{stars(raw.loc[a, 'p'])} ({f2(raw.loc[a, 'se'])})", p_fmt(raw.loc[a, "p_holm"]),
                     f"{sgn(pc.loc[a, 'premium'])}{stars(pc.loc[a, 'p'])} ({f2(pc.loc[a, 'se'])})"])
    tests = pd.read_csv(TAB / "rq1_tests.csv")
    tp = lambda s: float(tests.loc[tests.test.str.contains(s, regex=False), "p"].iloc[0])  # noqa: E731
    td = lambda s: float(tests.loc[tests.test.str.contains(s, regex=False), "dispersion"].iloc[0])  # noqa: E731
    n.update(shift_raw=f2(tp("quarterly raw")), shift_pc=f2(tp("per-person")), shift_psa=f2(tp("annual PSA")),
             shift_rel=f2(tp("relative to IDN-MYS-THA (")), disp_ratio=f"{td('dispersion ratio'):.1f}",
             disp_raw_a=f2(td("annual PSA")), disp_rel=f2(td("relative to IDN-MYS-THA (")))
    n["h1a"] = "supported" if tp("quarterly raw") < 0.05 else "not supported"
    n["h1b"] = "supported" if td("dispersion ratio") < 0.5 else "not supported"
    t["rq1"] = md_table(pd.DataFrame(rows, columns=["Administration", "Quarters charged", "n", "Mean growth",
                                                    "Premium (s.e.)", "Holm p", "Per-person premium (s.e.)"]),
                        "Table 2. Administration premiums in quarterly real GDP growth, 1981Q2–" + n["mj_last"],
                        f"Growth at a compounded annual rate, percent; premium = administration mean minus the sample "
                        f"mean ({n['mean_q']}%). Newey–West standard errors (6 lags) in parentheses. \\* p < 0.10, "
                        f"\\*\\* p < 0.05, \\*\\*\\* p < 0.01 (unadjusted). Holm p corrects for the eight tests. "
                        f"Circular-shift test of no differences: p = {n['shift_raw']} (raw), {n['shift_pc']} (per person).")
    a1 = pd.read_csv(TAB / "rq1_premiums_a.csv")
    pv = a1.pivot(index="admin", columns="measure", values="premium")
    nv = a1.pivot(index="admin", columns="measure", values="n")
    for a in pv.index:
        n[f"rel_{a}"] = sgn(pv.loc[a, "g_rel"])
        n[f"pa_{a}"] = sgn(pv.loc[a, "g_psa"])
    rows = [[NAME[a], int(nv.loc[a, "g_psa"]), sgn(pv.loc[a, "g_psa"]), sgn(pv.loc[a, "g_rel"]),
             "" if pd.isna(pv.loc[a, "g_rel4"]) else sgn(pv.loc[a, "g_rel4"])] for a in ORDER]
    pa = pd.read_parquet("data/processed/panel_a.parquet")
    n["peers_pre97"], n["peers_post97"] = f"{pa.loc[1962:1996, 'g_peers'].mean():.1f}", f"{pa.loc[1997:2025, 'g_peers'].mean():.1f}"
    n["ph_pre97"], n["ph_post10"] = f"{pa.loc[1962:1996, 'g_wb'].mean():.1f}", f"{pa.loc[2011:2025, 'g_wb'].mean():.1f}"
    t["rq1a"] = md_table(pd.DataFrame(rows, columns=["Administration", "Years", "Premium, PSA growth",
                                                     "Premium relative to IDN–MYS–THA", "Relative to IDN–MYS–THA–VNM"]),
                         "Table 3. Annual premiums, raw and relative to regional peers, 1962–2025",
                         f"Percentage points. Years charged to the administration in office for most of the year after a "
                         f"one-quarter lag. Dispersion of premiums: {n['disp_raw_a']} (raw), {n['disp_rel']} (relative). "
                         f"Shift-test p: {n['shift_psa']} (raw), {n['shift_rel']} (relative). Vietnam data start in 1985, so "
                         f"the last column covers only 1985 for Marcos Sr.")

    # ---- RQ2 -------------------------------------------------------------------------------
    j = pd.read_csv(TAB / "rq2_joint.csv").set_index("admin")
    sm = pd.read_csv(TAB / "rq2_summary.csv").set_index("item")["value"]
    sv = lambda k: float(sm[k])  # noqa: E731
    n.update(S=f2(sv("share of premium dispersion explained by luck, S")), joint_sample=sm["joint sample"],
             joint_n=int(float(sm["quarters"])), wald_all=p_fmt(sv("Wald test all shock lags = 0, p")),
             wald_oil=p_fmt(sv("Wald test oil lags = 0, p")), wald_us=p_fmt(sv("Wald test us lags = 0, p")),
             wald_elnino=p_fmt(sv("Wald test elnino lags = 0, p")), wald_ebp=p_fmt(sv("Wald test ebp lags = 0, p")),
             sum_us=f2(sv("sum of us lag coefficients")), sum_ebp=f2(sv("sum of ebp lag coefficients")),
             sum_oil=f2(sv("sum of oil lag coefficients")), sum_elnino=f2(sv("sum of elnino lag coefficients")),
             r2=f2(sv("R2")))
    S = sv("share of premium dispersion explained by luck, S")
    n["h2"] = ("H2b (more than half)" if S > 0.65 else "H2a (about half)" if S >= 0.35 else "neither hypothesis")
    for a, r in j.iterrows():
        n[f"j_{a}_P"], n[f"j_{a}_E"], n[f"j_{a}_Ese"], n[f"j_{a}_U"] = sgn(r.premium), sgn(r.explained), f2(r.explained_se), sgn(r.unexplained)
        n[f"j_{a}_us"], n[f"j_{a}_oil"], n[f"j_{a}_ebp"] = sgn(r.explained_us), sgn(r.explained_oil), sgn(r.explained_ebp)
    rows = [[NAME[a] + (" (1983–86)" if a == "marcos_sr" else ""), int(j.loc[a, "n"]), sgn(j.loc[a, "premium"]),
             f"{sgn(j.loc[a, 'explained'])} ({f2(j.loc[a, 'explained_se'])})", sgn(j.loc[a, "unexplained"]),
             sgn(j.loc[a, "explained_oil"]), sgn(j.loc[a, "explained_us"]), sgn(j.loc[a, "explained_elnino"]),
             sgn(j.loc[a, "explained_ebp"])] for a in j.index]
    t["rq2"] = md_table(pd.DataFrame(rows, columns=["Administration", "n", "Premium", "Explained (s.e.)", "Unexplained",
                                                    "Oil", "US demand", "El Niño", "Financial"]),
                        f"Table 4. How much of each premium is luck? Joint shock model, {n['joint_sample']}",
                        f"Percentage points. Explained = the administration's average of the fitted shock component minus "
                        f"its sample average; the last four columns split it by shock. Each shock enters with lags 0–6. "
                        f"Share of the dispersion of premiums explained, S = {n['S']}. Wald tests that a shock's lags are "
                        f"all zero: oil p = {n['wald_oil']}, US demand p = {n['wald_us']}, El Niño p = {n['wald_elnino']}, "
                        f"financial conditions p = {n['wald_ebp']}.")

    # ---- robustness ---------------------------------------------------------------------------
    rob = pd.read_csv(TAB / "robustness.csv")
    specs = rob.groupby("spec", sort=False)[["shift_p", "S"]].first()
    n["S_ex_debt"] = f2(specs.loc["excluding 1984Q1-1985Q4", "S"])
    n["S_partners"] = f2(specs.loc["foreign demand US-JP-EA (from 1997)", "S"])
    lagS = specs.loc[[s for s in specs.index if s.startswith("timing lag")], "S"]
    n["S_lag_min"], n["S_lag_max"] = f2(lagS.min()), f2(lagS.max())
    n["shift_min"] = f2(specs["shift_p"].min())
    for a in ["aquino_b", "marcos_jr"]:
        r = rob[rob.admin == a]["premium_raw"]
        n[f"rob_{a}_min"], n[f"rob_{a}_max"] = f2(r.min()), f2(r.max())
    piv = rob.pivot_table(index="spec", columns="admin", values="premium_raw", sort=False)
    rows = [[s[0].upper() + s[1:], f2(specs.loc[s, "shift_p"]), f2(specs.loc[s, "S"]), sgn(piv.loc[s, "aquino_b"]), sgn(piv.loc[s, "marcos_jr"])]
            for s in specs.index]
    t["rob"] = md_table(pd.DataFrame(rows, columns=["Specification", "Shift-test p", "Luck share S",
                                                    "Aquino III premium", "Marcos Jr. premium"]),
                        "Table 7. Robustness", "All checks were specified before estimation. Premiums are raw quarterly "
                        "premiums (percentage points).")

    # ---- RQ3 -------------------------------------------------------------------------------
    r3 = pd.read_csv(TAB / "rq3_inheritance.csv").set_index("admin")
    n["mean4q"] = f2(r3["mean_4q_growth"].iloc[0])
    for a, r in r3.iterrows():
        n[f"r3_{a}_act"], n[f"r3_{a}_ar"], n[f"r3_{a}_bb"] = f2(r.actual), f2(r["forecast_AR"]), f2(r["forecast_bounce-back AR"])
        n[f"r3_{a}_h3"] = "yes" if r.H3_inherited else "no"
    n["h3_aquino_c"] = "supported" if r3.loc["aquino_c", "H3_inherited"] else "not supported"
    n["h3_marcos_jr"] = "supported" if r3.loc["marcos_jr", "H3_inherited"] else "not supported"
    rows = [[NAME[a], r.origin, f2(r.actual), f2(r["forecast_AR"]), f2(r["forecast_bounce-back AR"]),
             "yes" if r.H3_inherited else "no"] for a, r in r3.iterrows()]
    t["rq3"] = md_table(pd.DataFrame(rows, columns=["Administration", "Forecast made in", "Actual first-year growth",
                                                    "AR forecast", "Bounce-back forecast", "Inherited (H3 rule)"]),
                        "Table 5. Was first-year growth inherited?",
                        f"Growth over the first four charged quarters, 100·ln(GDP_s+3 / GDP_s−1), percent. Sample mean "
                        f"{n['mean4q']}%. 'Inherited' if the bounce-back forecast exceeds the mean by at least half of the "
                        f"actual excess.")

    # ---- RQ4 -------------------------------------------------------------------------------
    r4 = pd.read_csv(TAB / "rq4_same_point.csv").set_index("admin")
    ok = r4.dropna(subset=["raw_mean"])
    for a, r in ok.iterrows():
        n[f"r4_{a}_raw"], n[f"r4_{a}_adj"] = f2(r.raw_mean), f2(r.luck_adjusted_mean)
    z = (ok[["raw_mj_minus_this", "luck_adjusted_mj_minus_this"]].abs().values /
         ok[["raw_se", "luck_adjusted_se"]].values)
    n["r4_max_t"] = f"{np.nanmax(z):.1f}"
    rows = []
    for a, r in ok.iterrows():
        d = "" if a == "marcos_jr" else f"{sgn(r.raw_mj_minus_this)} ({f2(r.raw_se)})"
        da = "" if a == "marcos_jr" else f"{sgn(r.luck_adjusted_mj_minus_this)} ({f2(r.luck_adjusted_se)})"
        rows.append([NAME[a], f"{r['first']}–{r['last']}", f2(r.raw_mean), d, f2(r.luck_adjusted_mean), da])
    t["rq4"] = md_table(pd.DataFrame(rows, columns=["Administration", "First 15 quarters", "Raw mean",
                                                    "Marcos Jr. minus this (s.e.)", "Luck-adjusted mean",
                                                    "Marcos Jr. minus this (s.e.)"]),
                        "Table 6. The same point in the term: the first 15 quarters",
                        "Percent, annual rate. Luck-adjusted growth removes the fitted shock component of the joint model. "
                        "Estrada (10 quarters) and Marcos Sr. (first quarters outside the sample) are not compared. "
                        "Newey–West standard errors; the luck-adjusted ones ignore the estimation error of the shock component.")

    # ---- scorecard -----------------------------------------------------------------------------
    sc = pd.read_csv(TAB / "scorecard.csv")
    meas = {"g_psa": "GDP growth", "gpc_wb": "Growth per person", "g_rel": "Relative to peers",
            "inflation": "Inflation", "unemployment": "Unemployment (1991–)"}
    for _, r in sc[sc.admin == "marcos_jr"].iterrows():
        n[f"sc_mj_{r.measure}"], n[f"sc_mj_{r.measure}_z"] = f2(r["mean"]), sgn(r.z)
    m = sc.pivot(index="admin", columns="measure", values="mean")
    zz = sc.pivot(index="admin", columns="measure", values="z")
    rows = []
    for a in ORDER:
        rows.append([NAME[a]] + ["" if pd.isna(m.loc[a, k]) else f"{f2(m.loc[a, k])} ({sgn(zz.loc[a, k])})" for k in meas])
    t["score"] = md_table(pd.DataFrame(rows, columns=["Administration"] + list(meas.values())),
                          "Table 8. Scorecard, annual averages 1962–2025 (z-score in parentheses)",
                          "Percent; z = (administration mean − 1962–2025 mean) / standard deviation of the annual values. "
                          "For inflation and unemployment a negative z means a lower rate than usual. No composite index is "
                          "formed and administrations are not ranked. Unemployment is the ILO modelled estimate (1991–).")
    return n, t


if __name__ == "__main__":
    n, t = build()
    (TAB / "paper_numbers.json").write_text(json.dumps(n, indent=1, ensure_ascii=False))
    render("paper/manuscript_template.md", "paper/manuscript.md", numbers=TAB / "paper_numbers.json",
           bib="paper/references.bib", resource_path="paper:output/figures", tables=t)
    render("docs/statistical_annex_template.md", "docs/statistical_annex.md", numbers=TAB / "paper_numbers.json",
           resource_path="docs:output/figures", tables=t)
