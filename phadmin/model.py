"""Administration premiums, the shock regression and randomization tests (decision D7).

Model: y_t = sum_a alpha_a A_{a,t} + sum_k sum_{j in lags} gamma_kj e_{k,t-j} + u_t.
The explained premium of group a is the a-average of the fitted shock component
c_t = sum gamma_hat e minus its sample average (Blinder and Watson, footnote 19, Table 7).
Standard errors: Newey-West (Bartlett) with 6 lags.
"""
import itertools

import numpy as np
import pandas as pd
import statsmodels.api as sm

NW_LAGS = 6


def nw_fit(y, X):
    return sm.OLS(y, X).fit(cov_type="HAC", cov_kwds={"maxlags": NW_LAGS})


def premiums(y, labels):
    """Raw premium of each group: group mean minus sample mean. Returns DataFrame
    (n, mean, premium)."""
    d = pd.concat([y.rename("y"), labels.rename("g")], axis=1).dropna()
    g = d.groupby("g", sort=False)["y"].agg(["count", "mean"]).rename(columns={"count": "n"})
    g["premium"] = g["mean"] - d["y"].mean()
    return g


def gap_nw(y, is_a):
    """Difference of means (a minus not a) with a Newey-West s.e. from y on const + dummy."""
    d = pd.concat([y.rename("y"), is_a.astype(float).rename("a")], axis=1).dropna()
    r = nw_fit(d["y"], sm.add_constant(d[["a"]]))
    return r.params["a"], r.bse["a"]


def lagged(e, lags, name):
    return pd.DataFrame({f"{name}_l{j}": e.shift(j) for j in lags})


def shock_model(y, labels, shocks, lags):
    """Fit the shock regression. shocks: dict name -> Series. Returns dict with the fit,
    the fitted shock component c (total and per shock) and the sample used."""
    groups = pd.get_dummies(labels, dtype=float)
    Xs = pd.concat([lagged(s, lags, k) for k, s in shocks.items()], axis=1)
    d = pd.concat([y.rename("y"), groups, Xs], axis=1)
    d = d[labels.reindex(d.index).notna()].dropna()
    gcols = [c for c in groups.columns if d[c].sum() > 0]
    scols = list(Xs.columns)
    r = nw_fit(d["y"], d[gcols + scols])
    comp = {k: d[[c for c in scols if c.startswith(k + "_l")]] @ r.params[[c for c in scols if c.startswith(k + "_l")]]
            for k in shocks}
    return {"fit": r, "data": d, "gcols": gcols, "scols": scols, "comp": comp,
            "c": sum(comp.values()), "labels": labels.reindex(d.index)}


def explained(m, contrast, shock=None):
    """Explained part of a contrast between groups.

    contrast: dict group -> weight, defining a linear contrast of group averages of c,
    e.g. {"D": 1, "R": -1} for the D-R gap, or a premium (group a minus the sample mean,
    which is handled by passing contrast="premium:<a>"). Returns (estimate, s.e.) with the
    s.e. from the HAC covariance of gamma_hat, holding the shock averages fixed."""
    d, lab, r = m["data"], m["labels"], m["fit"]
    cols = [c for c in m["scols"] if shock is None or c.startswith(shock + "_l")]
    X = d[cols]
    if isinstance(contrast, str) and contrast.startswith("premium:"):
        a = contrast.split(":", 1)[1]
        w = X[lab == a].mean() - X.mean()
    else:
        w = sum(wt * X[lab == g].mean() for g, wt in contrast.items())
    est = float(w @ r.params[cols])
    V = r.cov_params().loc[cols, cols]
    return est, float(np.sqrt(w @ V @ w))


def term_effects(m, shock=None):
    """Average of the fitted shock component by group, minus its sample average (Table 7)."""
    c = m["c"] if shock is None else m["comp"][shock]
    return c.groupby(m["labels"], sort=False).mean() - c.mean()


def block_randomization_p(y, block_ids, block_party, n_a):
    """Exact randomization p-value for a two-group gap: every way of giving label A to n_a
    of the blocks. block_ids: Series mapping each observation to a block; block_party: Series
    block -> 'A'/'B' (actual). Two-sided: share of assignments with |gap| >= |actual|."""
    d = pd.concat([y.rename("y"), block_ids.rename("b")], axis=1).dropna()
    sums = d.groupby("b")["y"].agg(["sum", "count"])
    blocks = list(sums.index)
    actual_a = [b for b in blocks if block_party[b] == "A"]

    def gap(a_set):
        a = sums.loc[list(a_set)]
        b = sums.drop(index=list(a_set))
        return a["sum"].sum() / a["count"].sum() - b["sum"].sum() / b["count"].sum()

    g0 = gap(actual_a)
    allg = np.array([gap(c) for c in itertools.combinations(blocks, n_a)])
    return float(np.mean(np.abs(allg) >= abs(g0) - 1e-12)), g0


def between_ss(y, labels):
    d = pd.concat([y.rename("y"), labels.rename("g")], axis=1).dropna()
    m = d["y"].mean()
    g = d.groupby("g")["y"].agg(["count", "mean"])
    return float((g["count"] * (g["mean"] - m) ** 2).sum())


def shift_test_p(y, labels):
    """Circular-shift randomization test of 'no differences between administrations'.
    Slides the label calendar along y by every offset (keeping each administration's length
    and the order of terms) and compares the between-group sum of squares. p includes the
    actual alignment."""
    d = pd.concat([y.rename("y"), labels.rename("g")], axis=1).dropna()
    yv, lv = d["y"].reset_index(drop=True), d["g"].reset_index(drop=True)
    s0 = between_ss(yv, lv)
    stats = [between_ss(yv, pd.Series(np.roll(lv.values, k))) for k in range(len(lv))]
    return float(np.mean(np.array(stats) >= s0 - 1e-12)), s0
