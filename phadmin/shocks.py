"""Shock constructions (decisions D6, D12)."""
import numpy as np
import pandas as pd
import statsmodels.api as sm


def monthly_to_quarterly(s):
    """Quarterly average of a monthly series with a DatetimeIndex -> PeriodIndex (Q)."""
    s = s.copy()
    s.index = pd.PeriodIndex(s.index, freq="M")
    return s.groupby(s.index.asfreq("Q")).mean()


def hamilton_net_increase(o, window=12):
    """Hamilton (2003) net oil price increase: max(0, 100*ln(O_t / max(O_{t-window..t-1}))).
    Uses the available history when fewer than `window` past quarters exist."""
    prev_max = o.shift(1).rolling(window, min_periods=1).max()
    return np.maximum(0.0, 100 * np.log(o / prev_max))


def purge(e, y, own_lags=4, y_lags=4):
    """Residual of e_t on a constant, e_{t-1..t-own_lags} and y_{t..t-y_lags}: removes the
    part of a foreign series that is predictable from its own past or from domestic growth
    (Blinder and Watson's treatment of European growth)."""
    X = {f"e_l{j}": e.shift(j) for j in range(1, own_lags + 1)}
    X.update({f"y_l{j}": y.shift(j) for j in range(0, y_lags + 1)})
    X = pd.DataFrame(X)
    d = pd.concat([e.rename("e"), X], axis=1).dropna()  # rows where both e and y lags exist
    res = sm.OLS(d["e"], sm.add_constant(d.drop(columns="e"))).fit()
    return res.resid.reindex(e.index)
