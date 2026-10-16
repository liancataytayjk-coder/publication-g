"""Simulation and unit tests for phadmin (Phase 3.1). Run with pytest before any estimate."""
import numpy as np
import pandas as pd
import pytest

from phadmin.calendar import charge_quarters, charge_years
from phadmin.model import (block_randomization_p, explained, premiums, shift_test_p,
                           shock_model, term_effects)
from phadmin.shocks import hamilton_net_increase, purge

ADMIN = pd.read_csv("data/manual/administrations.csv", parse_dates=["start_date"])
PH_TERMS = ADMIN.rename(columns={"admin_id": "label", "start_date": "start"})[["label", "start"]]


def test_philippine_calendar_examples():
    q = pd.period_range("1981Q1", "2026Q2", freq="Q")
    s = charge_quarters(PH_TERMS, q, lag=1)
    first = s.groupby(s, sort=False).apply(lambda x: x.index.min())
    assert str(first["aquino_c"]) == "1986Q3"   # 25 Feb 1986: Marcos held most of Q1 -> Q2 his
    assert str(first["ramos"]) == "1992Q4"      # 30 June inauguration
    assert str(first["estrada"]) == "1998Q4"
    assert str(first["arroyo"]) == "2001Q2"     # 20 Jan 2001
    assert str(first["aquino_b"]) == "2010Q4"
    assert str(first["duterte"]) == "2016Q4"
    assert str(first["marcos_jr"]) == "2022Q4"


def test_lag_zero_charges_inauguration_quarter_by_majority():
    s = charge_quarters(PH_TERMS, pd.period_range("1992Q1", "1993Q1", freq="Q"), lag=0)
    assert s[pd.Period("1992Q2")] == "aquino_c" and s[pd.Period("1992Q3")] == "ramos"


def test_us_calendar_truman2_starts_1949q2():
    terms = pd.DataFrame({"label": ["Tr1", "Tr2", "Ei1"],
                          "start": pd.to_datetime(["1945-04-12", "1949-01-20", "1953-01-20"])})
    s = charge_quarters(terms, pd.period_range("1949Q1", "1953Q2", freq="Q"), lag=1)
    assert s[pd.Period("1949Q1")] == "Tr1" and s[pd.Period("1949Q2")] == "Tr2"
    assert s[pd.Period("1953Q1")] == "Tr2" and s[pd.Period("1953Q2")] == "Ei1"
    assert (s == "Tr2").sum() == 16


def test_charge_years_ties_go_to_successor():
    q = pd.period_range("1986Q1", "1986Q4", freq="Q")
    lab = pd.Series(["marcos_sr", "marcos_sr", "aquino_c", "aquino_c"], index=q)
    lab.index = lab.index.to_timestamp()
    assert charge_years(lab)[1986] == "aquino_c"


def test_hamilton_measure():
    o = pd.Series([10, 12, 11, 15, 14, 9, 20.0])
    h = hamilton_net_increase(o, window=3)
    assert np.isnan(h.iloc[0]) or h.iloc[0] == 0
    assert h.iloc[1] == pytest.approx(100 * np.log(12 / 10))
    assert h.iloc[2] == 0                      # below previous max
    assert h.iloc[3] == pytest.approx(100 * np.log(15 / 12))
    assert h.iloc[6] == pytest.approx(100 * np.log(20 / 15))   # max of last 3 = 15


def simulate(seed=0, T=400, effects=(1.5, -1.0, 0.5, -1.0), gam=(-0.3, -0.2, -0.1)):
    rng = np.random.default_rng(seed)
    idx = pd.period_range("1900Q1", periods=T, freq="Q")
    n = T // len(effects)
    lab = pd.Series(np.repeat([f"a{i}" for i in range(len(effects))], n), index=idx[: n * len(effects)]).reindex(idx)
    e = pd.Series(np.maximum(0, rng.normal(0, 3, T)), index=idx)
    alpha = lab.map({f"a{i}": 3 + x for i, x in enumerate(effects)})
    c = sum(g * e.shift(j) for j, g in enumerate(gam))
    y = alpha + c + rng.normal(0, 1, T)
    return y, lab, e, c


def test_shock_model_recovers_lag_coefficients_and_explained_premiums():
    y, lab, e, c = simulate(T=2000)  # long sample: the s.e. of each gamma is about 0.013
    m = shock_model(y, lab, {"oil": e}, lags=range(0, 3))
    g = m["fit"].params[["oil_l0", "oil_l1", "oil_l2"]].values
    assert np.allclose(g, [-0.3, -0.2, -0.1], atol=0.06)
    # explained premium equals the group mean of the true shock component minus its mean
    d = m["data"].index
    true = c[d].groupby(lab[d]).mean() - c[d].mean()
    est = term_effects(m)
    assert np.allclose(est[true.index].values, true.values, atol=0.08)
    for a in true.index:
        v, se = explained(m, f"premium:{a}")
        assert v == pytest.approx(est[a], abs=1e-10) and se > 0


def test_explained_two_group_contrast_matches_difference_of_term_effects():
    y, lab, e, _ = simulate(seed=1)
    m = shock_model(y, lab, {"oil": e}, lags=range(1, 4))
    te = term_effects(m)
    v, _ = explained(m, {"a0": 1, "a1": -1})
    assert v == pytest.approx(te["a0"] - te["a1"], abs=1e-10)


def test_premiums_raw():
    y, lab, *_ = simulate(seed=2, effects=(1.0, -1.0, 1.0, -1.0), gam=(0, 0, 0))
    p = premiums(y, lab)
    assert np.allclose(p["premium"].values, [1, -1, 1, -1], atol=0.25)


def test_block_randomization_exact_and_powerful():
    rng = np.random.default_rng(3)
    blocks = np.repeat(np.arange(10), 8)
    party = pd.Series({b: ("A" if b % 2 == 0 else "B") for b in range(10)})
    y = pd.Series(rng.normal(0, 1, 80) + np.where(blocks % 2 == 0, 2.0, 0.0))
    p, g = block_randomization_p(y, pd.Series(blocks), party, 5)
    assert g > 1.5 and p <= 2 / 252 + 1e-9   # actual and its mirror are the two extremes
    y0 = pd.Series(rng.normal(0, 1, 80))
    p0, _ = block_randomization_p(y0, pd.Series(blocks), party, 5)
    assert p0 > 0.01


def test_shift_test_detects_effects_and_not_noise():
    y, lab, *_ = simulate(seed=4, effects=(2, -2, 2, -2), gam=(0, 0, 0))
    p, _ = shift_test_p(y, lab)
    assert p < 0.05
    rng = np.random.default_rng(5)
    ps = [shift_test_p(pd.Series(rng.normal(0, 1, len(lab)), index=lab.index), lab)[0] for _ in range(40)]
    assert 0.02 < np.mean(np.array(ps) < 0.10) < 0.25   # roughly nominal size


def test_purge_removes_domestic_feedback():
    rng = np.random.default_rng(6)
    T = 300
    y = pd.Series(rng.normal(0, 1, T))
    pure = pd.Series(rng.normal(0, 1, T))
    e = 0.8 * y + pure
    r = purge(e, y)
    ok = r.notna()
    assert abs(np.corrcoef(r[ok], y[ok])[0, 1]) < 1e-8
    assert np.corrcoef(r[ok], pure[ok])[0, 1] > 0.95
