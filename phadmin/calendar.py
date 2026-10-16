"""Charge each quarter to an administration (decision D4).

Rule: quarter t is charged to whoever held office for most of quarter t - lag.
With lag = 1 this is Blinder and Watson's convention for 20 January
inaugurations (the inauguration quarter goes to the predecessor), and it gives
the 30 June Philippine inaugurations the same lag of about one quarter.
"""
import pandas as pd


def charge_quarters(terms, quarters, lag=1):
    """terms: DataFrame with columns label, start (datetime), sorted by start; a term runs
    until the next start. quarters: PeriodIndex (freq Q). Returns a Series of labels."""
    terms = terms.sort_values("start").reset_index(drop=True)
    starts = list(pd.to_datetime(terms["start"]))
    labels = list(terms["label"])
    out = {}
    for q in quarters:
        ref = q - lag
        q0, q1 = ref.start_time.normalize(), (ref + 1).start_time.normalize()
        best, best_days = None, -1
        for i, lab in enumerate(labels):
            a = max(starts[i], q0)
            b = min(starts[i + 1] if i + 1 < len(starts) else q1, q1)
            days = (b - a).days
            if days > best_days:
                best, best_days = lab, days
        out[q] = best if best_days > 0 else None
    return pd.Series(out, name="admin")


def charge_years(quarter_labels):
    """A year goes to the administration charged in most of its quarters; ties go to the
    successor (the later administration)."""
    s = quarter_labels.dropna()
    res = {}
    for y, g in s.groupby(s.index.year):
        counts = g.value_counts()
        top = counts[counts == counts.max()].index
        res[y] = g[g.isin(top)].iloc[-1]  # latest among the tied labels
    return pd.Series(res, name="admin")
