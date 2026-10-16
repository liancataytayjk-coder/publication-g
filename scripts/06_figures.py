"""All figures, black and white, no titles (captions live in the documents).

fig1_growth_by_admin   quarterly growth 1981Q2-2026Q2 with administrations shaded
fig2_premiums_luck     raw, explained and unexplained premiums (joint model, RQ2)
fig3_peers             annual premiums: raw growth and growth relative to peers (RQ1)
fig4_inheritance       first-year growth: actual against AR and bounce-back forecasts (RQ3)
fig5_same_point        first 15 quarters: raw and luck-adjusted average growth (RQ4)
fig6_replication       Table 7 oil effects by US term: published against ours (gate)
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fig_style import A, B, BLACK, LIGHT, MID, save, setup, zero  # noqa: E402

OUT, TAB, PROC = Path("output/figures"), Path("output/tables"), Path("data/processed")
setup()
SHORT = pd.read_csv("data/manual/administrations.csv").set_index("admin_id")["short"].to_dict()
ORDER = ["macapagal", "marcos_sr", "aquino_c", "ramos", "estrada", "arroyo", "aquino_b", "duterte", "marcos_jr"]
SHORT["marcos_sr"] = "Marcos Sr."


def wrap(a):
    return SHORT[a].replace(" ", "\n")

# fig1 -------------------------------------------------------------------------------------
pq = pd.read_parquet(PROC / "panel_q.parquet").loc["1981Q2":]
x = pq.index.to_timestamp()
fig, ax = plt.subplots(figsize=(6.5, 3.0))
cal = pd.read_csv(TAB / "admin_calendar.csv")
for i, r in cal.iterrows():
    a, b = pd.Period(max(r["first"], "1981Q2")).start_time, pd.Period(r["last"]).end_time
    if i % 2 == 0:
        ax.axvspan(a, b, color=LIGHT, linewidth=0)
    ax.text(a + (b - a) / 2, 37, SHORT[r["admin"]], ha="center", va="bottom", fontsize=7)
ax.plot(x, pq["y"].clip(lower=-30), color=BLACK, linewidth=0.9)
ax.axhline(pq["y"].mean(), color=BLACK, linestyle="--", linewidth=0.7)
zero(ax)
ax.set_ylim(-32, 44)
ax.set_ylabel("Percent, annual rate")
ax.annotate("2020Q2: −44", xy=(pd.Timestamp("2020-05-15"), -30), xytext=(pd.Timestamp("2010-01-01"), -27),
            fontsize=7, arrowprops=dict(arrowstyle="-", color=BLACK, linewidth=0.5))
save(fig, "fig1_growth_by_admin", OUT)

# fig2 -------------------------------------------------------------------------------------
j = pd.read_csv(TAB / "rq2_joint.csv").set_index("admin")
j = j.reindex([a for a in ORDER if a in j.index])
pos = np.arange(len(j))
fig, ax = plt.subplots(figsize=(6.5, 3.0))
w = 0.27
ax.bar(pos - w, j["premium"], w, color="white", edgecolor=BLACK, linewidth=0.7, label="Raw premium")
ax.bar(pos, j["explained"], w, color=MID, edgecolor=BLACK, linewidth=0.7, label="Explained by luck")
ax.errorbar(pos, j["explained"], yerr=1.96 * j["explained_se"], fmt="none", ecolor=BLACK, elinewidth=0.6, capsize=2)
ax.bar(pos + w, j["unexplained"], w, color="white", edgecolor=BLACK, hatch="////", linewidth=0.7, label="Unexplained")
zero(ax)
ax.set_xticks(pos, [wrap(a) + ("\n(1983–86)" if a == "marcos_sr" else "") for a in j.index], fontsize=7)
ax.set_ylabel("Percentage points")
ax.legend(loc="lower right", fontsize=7)
save(fig, "fig2_premiums_luck", OUT)

# fig3 -------------------------------------------------------------------------------------
a = pd.read_csv(TAB / "rq1_premiums_a.csv")
p = a.pivot(index="admin", columns="measure", values="premium").reindex(ORDER)
fig, ax = plt.subplots(figsize=(6.5, 3.0))
pos = np.arange(len(p))
ax.bar(pos - 0.2, p["g_psa"], 0.4, color="white", edgecolor=BLACK, linewidth=0.7, label="Philippine growth")
ax.bar(pos + 0.2, p["g_rel"], 0.4, color=MID, edgecolor=BLACK, linewidth=0.7,
       label="Growth relative to Indonesia, Malaysia and Thailand")
zero(ax)
ax.set_xticks(pos, [wrap(x) for x in p.index], fontsize=7)
ax.set_ylabel("Percentage points")
ax.legend(loc="lower right", fontsize=7)
save(fig, "fig3_peers", OUT)

# fig4 -------------------------------------------------------------------------------------
r3 = pd.read_csv(TAB / "rq3_inheritance.csv").set_index("admin")
pos = np.arange(len(r3))
fig, ax = plt.subplots(figsize=(6.5, 3.0))
ax.bar(pos, r3["actual"], 0.5, color=LIGHT, edgecolor=BLACK, linewidth=0.7, label="Actual")
ax.plot(pos, r3["forecast_AR"], linestyle="none", marker="o", color=BLACK, markersize=5, label="AR forecast")
ax.plot(pos, r3["forecast_bounce-back AR"], linestyle="none", marker="s", color=BLACK, markerfacecolor="white",
        markersize=5, label="Bounce-back forecast")
ax.axhline(r3["mean_4q_growth"].iloc[0], color=BLACK, linestyle="--", linewidth=0.7, label="Sample mean")
ax.set_xticks(pos, [SHORT[x] for x in r3.index], fontsize=7)
ax.set_ylabel("Growth over first four quarters, %")
ax.legend(loc="upper left", fontsize=7, ncol=2)
save(fig, "fig4_inheritance", OUT)

# fig5 -------------------------------------------------------------------------------------
r4 = pd.read_csv(TAB / "rq4_same_point.csv").dropna(subset=["raw_mean"]).set_index("admin")
pos = np.arange(len(r4))
fig, ax = plt.subplots(figsize=(6.0, 3.0))
ax.plot(pos, r4["raw_mean"], linestyle="none", label="Raw", **{k: v for k, v in A.items() if k != "linestyle"})
ax.plot(pos, r4["luck_adjusted_mean"], linestyle="none", label="Luck-adjusted",
        **{k: v for k, v in B.items() if k != "linestyle"})
zero(ax)
ax.set_xticks(pos, [SHORT[x] for x in r4.index], fontsize=7)
ax.set_ylabel("Average growth, first 15 quarters, %")
ax.legend(loc="lower left", fontsize=7)
save(fig, "fig5_same_point", OUT)

# fig6 -------------------------------------------------------------------------------------
rt = pd.read_csv(TAB / "replication_term_effects.csv")
fig, ax = plt.subplots(figsize=(3.4, 3.2))
ax.plot(rt["published"], rt["estimate"], linestyle="none", marker="o", color=BLACK, markersize=4)
lim = [-2.7, 1.2]
ax.plot(lim, lim, color=BLACK, linestyle=":", linewidth=0.7)
for _, r in rt[(rt["published"] < 0.3) | ((rt["estimate"] - rt["published"]).abs() > 0.15)].iterrows():
    ax.annotate(r["term"], (r["published"], r["estimate"]), fontsize=6, xytext=(3, -3), textcoords="offset points")
ax.set_xlabel("Blinder and Watson, Table 7")
ax.set_ylabel("This study")
save(fig, "fig6_replication", OUT)
print("figures written to", OUT)
