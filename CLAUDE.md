# Presidents and the Philippine economy: project brief

**Working title.** *Good policy or good luck? Philippine economic performance
across presidential administrations, 1961–2026.*

The study asks whether the Philippine economy has performed differently under
different presidents, how much of each administration's record is explained by
"luck" (shocks that no Philippine president controls, such as world oil prices,
growth in export markets and El Niño droughts), and where the current
administration stands once performance is put on a common footing. It
replicates the design of Blinder and Watson (2016, *American Economic Review*
106(4), 1015–1045, doi:10.1257/aer.20140913), "Presidents and the US economy:
an econometric exploration", on Philippine data. Unit: the Philippines,
quarterly 1981–2026 (main) and annual 1961–2025 (long view). Output: a journal
manuscript (personal research), separate from the inflation-forecasting study in
`publication-f`. Candidate journals (to be confirmed): *The Philippine Review of
Economics*, *Asian Economic Journal*, *Journal of Asian Economics*. The user
chose the topic (the economy under different administrations, including the
current one) on 2026-10-16 and delegated the reference paper.

## Conventions

- `data/raw/` holds untouched downloads only. Every file gets an entry in
  `data/raw/source_log.md` (URL, date pulled, base year, coverage).
- `data/manual/` holds small tables typed by hand from a cited source (for
  example the presidents' term dates). Each row names its source.
- `data/processed/` and `output/` are written by scripts, never by hand.
- `replication/blinder_watson2016_targets.csv` holds the reference paper's targets.
- No Philippine estimate is reported until the replication gate passes.
- Every specification choice goes in the decisions log below, with the
  evidence. Each is labelled pre-registered, supplementary or exploratory.
- Documents are rendered from templates. Never edit a rendered .md/.docx by hand.
- User style: as simple as possible. Define every term on first use (words →
  formula → example). Prefer paragraphs to bullets and tables.
- Neutral language about every president. The study measures; it does not rank
  people. Every claim about an administration is tied to a number and its
  uncertainty, and the luck-adjusted figure is always shown next to the raw one.

## Research questions and hypotheses

**Main question.** Did the Philippine economy grow faster under some presidents
than others, and how much of the difference is luck rather than policy?

Two terms are used throughout. The **administration premium** is an
administration's average growth minus the average over the whole sample:
P_a = ȳ_a − ȳ. For example, if growth averaged 4.0% over 1981–2026 and 5.0%
under one president, that president's premium is +1.0 point. The **explained
premium** is the part of P_a that the luck shocks account for; the
**unexplained premium** is the rest. The unexplained premium is an upper bound
on what policy could have contributed, because it also contains any luck we
fail to measure.

- **RQ1 (the facts).** Do administration premiums in real GDP growth differ
  more than chance would produce, on raw data and once growth is standardized
  (per person, and relative to regional peers)?
  - *H1a (as in the United States):* the differences are large and
    statistically detectable, even with few administrations.
  - *H1b (common regional shocks):* once growth is measured relative to
    Indonesia, Malaysia and Thailand, most of the difference disappears, because
    the big swings (the 1983–85 debt crisis aside) were regional: 1997–98, 2009,
    2020.
- **RQ2 (luck).** How much of each administration's premium is explained by
  shocks no Philippine president controls: oil prices, growth in export
  markets, El Niño and global financial conditions?
  - *H2a (as in Blinder and Watson):* about half of the dispersion of
    premiums is luck.
  - *H2b (small open economy):* more than half, because a small, open,
    oil-importing, typhoon- and drought-exposed economy depends more on outside
    shocks than the United States does.
- **RQ3 (inheritance).** Is early-term performance inherited? We compare growth
  in each administration's first year with forecasts made at its start (an
  autoregressive model and a "bounce-back" model that lets growth rebound after
  recessions).
  - *H3:* administrations that took over during or just after a collapse
    (C. Aquino in 1986, Marcos Jr. after the pandemic) show high early growth
    that the bounce-back forecast predicts, so it is inherited, not earned.
- **RQ4 (the current administration).** Where does the Marcos Jr.
  administration (2022 onwards, incomplete term) stand on raw and luck-adjusted
  premiums, compared with its predecessors at the same point in their terms?
  Descriptive, with uncertainty stated.

**Objectives.** Objective 1 (descriptive) is a standardized scorecard of every
administration since 1961: growth per person, growth relative to peers,
inflation, unemployment, with z-scores so that the measures share one scale.
Objective 2 (estimation) answers RQ1–RQ4. Objective 3 (policy) asks what share
of an administration's record is within a president's control, and proposes how
voters, media and analysts should read headline growth claims (always next to
the luck-adjusted figure).

## Reference specification (Blinder and Watson 2016)

Read from the NBER working-paper version (w20324, July 2014, downloaded from
nber.org on 2026-10-16; the PDF is not committed, for copyright). The
AER version itself is blocked here (403); see Open questions.

- **Outcome.** Quarterly real GDP growth at an annual rate, US national accounts,
  1947Q1–2013Q1. The main sample is the 16 complete four-year terms from
  Truman-2 to Obama-1 (1949Q2–2013Q1; 256 quarters).
- **Timing.** "The first quarter of each president's term is attributed to the
  previous president" (p. 3). Lags of 0, 2, 3 and 4 quarters are checked and
  give smaller gaps (Appendix Table A.2).
- **Facts (Table 1).** Means by party with two standard errors: clustered by
  term, and Newey–West with 6 lags. A randomization p-value assigns 7 D and 9 R
  labels at random to the 16 four-year blocks. GDP: D 4.35, R 2.54, gap 1.80
  (NW s.e. 0.64; p = 0.01).
- **Trends and initial conditions (Tables 4, 5).** Deviations from flexible
  biweight-kernel trends; first-year growth against SPF, Greenbook, AR(4),
  VAR(4) and nonlinear AR forecasts made in the first quarter of each term.
- **Shocks (equation 1).** y_t = α·Dem_t + β·Rep_t + Σ_k γ_k(L)e_kt + u_t. The
  part of the gap explained by shock k is the difference between the D and R
  averages of γ̂_k(L)e_kt (footnote 19). Table 6 has one shock at a time;
  Table 7 gives each term's average of γ̂(L)e_t minus the sample average; Table
  10 combines shocks. Lag length: "the 6-lag benchmark" (footnote 23); whether
  this is lags 0–6 or 1–6 is not stated (open question, checked in the gate).
- **Oil shock (Hamilton 2003).** Net oil price increase,
  P_t = max{0, 100·ln(O_t / max(O_{t−12},…,O_{t−1}))}, quarters, O = PPI crude
  petroleum (BLS WPU0561), quarterly average of monthly data.
- **Other shocks.** Fernald utilization-adjusted TFP; Ramey and Fisher–Peters
  defense; European GDP growth (residual from 4 own lags and current + 4 lags of
  US growth, detrended); taxes; monetary policy; financial spreads; consumer
  expectations; uncertainty.
- **Headline finding.** Oil, TFP, defense (Korea) and international shocks
  jointly explain about half of the gap: 1.02 of 1.87 points (Table 10A line 1).
  Fiscal and monetary shocks explain none.

## Decisions log

| # | Date | Decision | Evidence / reason | Label |
| --- | --- | --- | --- | --- |
| D1 | 2026-10-16 | Reference paper: Blinder and Watson (2016, AER). Text and tables read from NBER WP 20324 (2014). | The canonical econometric study of economic performance by president; its US data are public (FRED/ALFRED), so a numeric replication gate is possible. User delegated the choice. | pre-registered |
| D2 | 2026-10-16 | The unit of comparison is the administration (president), not the party. The estimand is the administration premium P_a = ȳ_a − ȳ, and pairwise differences between administrations. | Philippine parties are weak and fluid: the nine presidents since 1961 came from seven different parties, and no party held the presidency in two consecutive administrations (`data/manual/administrations.csv`). The US two-party gap generalizes to K group means. Blinder and Watson's Table 4 (deviations from the sample mean) and Table 7 (term-by-term effects) are the exact templates. | pre-registered |
| D3 | 2026-10-16 | Main outcome: quarterly real GDP growth at an annual rate, 400·Δln GDP_t, seasonally adjusted. Source: IMF International Financial Statistics, Philippines real GDP, not seasonally adjusted, 1981Q1–2024Q3 (via DBnomics), extended to the latest quarter from PSA or IMF (Phase 2). We seasonally adjust it ourselves and check our adjusted growth against the IMF's adjusted series over 2000Q1–2024Q3 (gate: correlation of quarterly growth ≥ 0.90). | The longest official quarterly series reachable; PSA's own site blocks this container (403). The IMF adjusted series starts only in 2000. | pre-registered |
| D4 | 2026-10-16 | Timing: each quarter is charged to the president who held office for most of the *previous* quarter. For annual data, a year goes to the president charged in most of its quarters; ties go to the successor. Robustness: lags of 0, 2 and 4 quarters. | This reproduces Blinder and Watson's rule exactly for 20 January inaugurations, and gives the same lag of about one quarter for the Philippine 30 June inaugurations (the new president is charged from the October quarter). Examples: Ramos from 1992Q4; Arroyo from 2001Q2; C. Aquino from 1986Q3. | pre-registered |
| D5 | 2026-10-16 | Two samples. Main: quarterly 1981Q2–latest, covering the last five years of Marcos Sr. (labelled "Marcos Sr., 1981–86 only") through Marcos Jr. Long view: annual 1961–2025, Macapagal to Marcos Jr. The incomplete Marcos Jr. term enters with all quarters to date. A "same point in the term" comparison (each administration's first N quarters, where N is the number of Marcos Jr. quarters observed) is a robustness check. | Quarterly data start in 1981; annual World Bank data start in 1960. Comparing an incomplete term with complete ones is unfair unless we also compare like with like. | pre-registered |
| D6 | 2026-10-16 | Candidate luck shocks, fixed in Phase 2 before any Philippine estimate: (i) oil: the Hamilton net oil price increase on WPU0561, exactly as in the reference; (ii) foreign demand: real GDP growth of the main export markets (the United States, Japan and China as the data allow), purged of Philippine feedback as the reference does for Europe; (iii) weather: El Niño intensity, max(0, ONI) averaged over the quarter (NOAA Oceanic Niño Index); (iv) global financial conditions: one series, chosen in Phase 2 from the excess bond premium (Gilchrist–Zakrajšek) or US monetary policy shocks. Domestic fiscal policy, the BSP policy rate, coups and the 2020 lockdown are *not* treated as luck. | Each is outside a Philippine president's control and has a documented channel to Philippine output. Typhoon damage is a natural fifth shock, but no long official quarterly series is reachable here (open question). | pre-registered |
| D7 | 2026-10-16 | Estimator: y_t = Σ_a α_a·A_{a,t} + Σ_k γ_k(L)e_kt + u_t, with A_{a,t} = 1 in administration a's charged quarters. Lags as settled by the gate (G3). The explained premium of administration a is the a-average of γ̂(L)e_t minus its full-sample average (reference footnote 19, Table 7). Standard errors: Newey–West with 6 lags. Test of "no differences": a circular-shift randomization test that slides the calendar of administrations along the growth series by every possible offset and recomputes the spread of administration means. | The direct generalization of the reference's equation (1) to K administrations. With only 8–9 administrations, standard errors are fragile; the shift test keeps each administration's length and the order of terms, as the reference's random relabelling of four-year blocks does. | pre-registered |
| D8 | 2026-10-16 | Standardization for Objective 1 and RQ1: (i) per person (World Bank GDP per capita, constant 2015 US$); (ii) relative to peers: Philippine growth minus the average of Indonesia, Malaysia and Thailand (World Bank, annual); Vietnam added from 1985 as robustness; (iii) z-scores of each measure over 1961–2025, so growth, inflation and unemployment share one scale. | Peers face the same regional shocks (1997–98, 2009, 2020), so the peer gap removes much of the common luck without a model. | pre-registered |
| D9 | 2026-10-16 | Replication gate on US data at the paper's own data vintage (ALFRED GDPC1, vintage 2014-07-01), criteria below. | The vintage is available, so the gate can be numeric, not qualitative. | pre-registered |
| D10 | 2026-10-16 | Replaces the source in D3: the main outcome series is PSA's own quarterly GDP at constant 2018 prices, 1981Q1–2026Q2 (OpenSTAT `0952B5BQEQ1`). Our seasonal adjustment is checked against PSA's own seasonally adjusted GDP, 2000Q1–2026Q2 (`012B5BEXS1`), with the same pass rule (correlation of quarterly growth ≥ 0.90). The IMF series is kept as a cross-check only. | The OpenSTAT data API is reachable (only PSA's web pages sit behind a bot check). The long series equals PSA's current table over 2000–2026 exactly and the IMF copy to within 0.14 points of year-on-year growth, and it runs to 2026Q2 instead of 2024Q3. Changed before any estimate. | pre-registered |
| D11 | 2026-10-16 | User confirmations: peers Indonesia, Malaysia and Thailand (Vietnam as robustness); quarterly 1981 onwards as the main sample; the incomplete Marcos Jr. term also compared at the same point in each term. The `lian-signature-style` skill is dropped; the empirical-econ-study style applies. | User reply, 2026-10-16. | pre-registered |
| D13 | 2026-10-16 | All GDP growth rates are quarterly growth at a compounded annual rate, 100·[(GDP_t/GDP_{t−1})⁴ − 1], replacing 400·Δln GDP in D3 and in the gate text. Log growth is kept as robustness. | The first gate run failed G1: both party means were 0.13 too low, which is the average compounding term g²/200. With the compounded rate the means, gap, overall mean and standard deviations match the paper to two decimals. Fixed before any Philippine estimate. | pre-registered (correction) |
| D14 | 2026-10-16 | Shock lags 0–6 (current and six lags), by the gate's pre-set rule. | G3: lags 0–6 explain 0.481 and lags 1–6 0.479 of the target 0.50; 0–6 is closer. | pre-registered |
| D12 | 2026-10-16 | Shock series fixed (completes D6): (i) oil: Hamilton net oil price increase on WPU0561; (ii) foreign demand: US real GDP growth (GDPC1), purged of Philippine feedback by taking the residual from a regression on 4 own lags and current + 4 lags of Philippine growth, as the reference does for Europe; robustness from 1995: the equal-weight average of US, Japan and euro-area growth, purged the same way; (iii) El Niño: max(0, ONI) averaged over the quarter; (iv) financial conditions: the Gilchrist–Zakrajšek excess bond premium, quarterly average, purged like (ii), available from 1973. | These are the long quarterly series that can be downloaded here. No quarterly GDP for Japan before 1994 or China before 2011 is reachable, so the main foreign-demand shock uses the United States, the largest export market for most of the sample. Fixed before any Philippine estimate. | pre-registered |

## Replication gate (pre-registered 2026-10-16, before any estimate)

Data: ALFRED real GDP (GDPC1, vintage 2014-07-01); PPI crude petroleum
(WPU0561, current vintage, quarterly average of monthly values). Terms Truman-2
to Obama-1, 1949Q2–2013Q1, first quarter of each term charged to the
predecessor. Growth 400·Δln GDP.

- **G1 (facts).** D–R gap in average growth ∈ [1.70, 1.90] (target 1.80), with
  the D mean ∈ [4.25, 4.45] (4.35) and the R mean ∈ [2.44, 2.64] (2.54).
- **G2 (inference).** Newey–West (6 lags) s.e. of the gap ∈ [0.54, 0.74]
  (target 0.64), and the randomization p-value from relabelling the 16 blocks
  ≤ 0.03 (target 0.01).
- **G3 (oil shock).** Gap explained by the Hamilton shock ∈ [0.40, 0.60]
  (target 0.50; Table 6 line 1). Both readings of "6 lags" are run (lags 0–6
  and 1–6). G3 passes if either lands in range; the one that does (or, if both
  do, the one closer to the target) becomes the lag rule for the Philippines.
- **G4 (shape).** Term-by-term oil effects (Table 7 line 1): correlation with
  the 16 published values ≥ 0.90 and the same sign in at least 14 of 16 terms.

The gate passes if G1–G4 all hold. If it fails, stop, re-read the specification,
fix the code and record what changed. Pass ranges are not loosened after the
results are seen.

**Result (2026-10-16): PASS on the second run** (`output/tables/replication_gate.csv`,
`scripts/04_replicate.py`). First run: FAIL on G1. The D–R gap (1.75), G2, G3
(0.47) and G4 passed, but both party means were about 0.13 too low (D 4.19, R
2.44), because the gate text above assumed log growth, 400·Δln GDP. The paper's
"annualized growth" is the compounded rate, 100·[(GDP_t/GDP_{t−1})⁴ − 1]; the
difference, about g²/200 on average, is exactly the shortfall. Fix (D13): all GDP
growth rates use the compounded rate. Pass ranges unchanged. Second run: D 4.346,
R 2.543, gap 1.803 (overall mean 3.332 against the paper's 3.33; s.d. 3.83 and
3.94 against "3.8 and 3.9"); NW s.e. 0.637; randomization p = 0.011; oil-explained
gap 0.481 with lags 0–6 (0.479 with lags 1–6), so lags 0–6 are adopted (D14);
term-by-term oil effects correlate 0.996 with Table 7, same sign in 16 of 16.

## Estimation plan (pre-specified 2026-10-16, after the gate, before any Philippine estimate)

**Common settings.** Outcome y_t: Philippine real GDP growth, quarterly, at a
compounded annual rate (D13), from PSA's constant-2018-price series adjusted by
X-13ARIMA-SEATS (log, automatic outliers, no trading-day effects; D10; our
adjusted growth correlates 0.978 with PSA's own adjusted series, 2000Q2–2026Q2,
`output/tables/sa_check.csv`). Sample 1981Q2–2026Q2 (181 quarters). Quarters are
charged by D4 (lag 1): Marcos Sr. 1981Q2–1986Q2 (21 quarters), C. Aquino
1986Q3–1992Q3 (25), Ramos 1992Q4–1998Q3 (24), Estrada 1998Q4–2001Q1 (10), Arroyo
2001Q2–2010Q3 (38), Aquino III 2010Q4–2016Q3 (24), Duterte 2016Q4–2022Q3 (24),
Marcos Jr. 2022Q4–2026Q2 (15, incomplete). Standard errors: Newey–West, 6 lags.
Shock lags: 0–6 (D14). Multiple testing: within each table of eight
administration premiums, p-values are also reported with a Holm correction.

**RQ1 (facts).** (a) Raw premium P_a = ȳ_a − ȳ for each administration, with
an NW s.e. (from the regression of y on a constant and the administration's
dummy, scaled by (n − n_a)/n). (b) The circular-shift test of "no differences"
(D7) on the between-administration sum of squares. H1a is supported if the
shift-test p < 0.05. (c) Per person: y_t minus that year's population growth
(World Bank SP.POP.TOTL); same statistics. (d) Long view and peers, annual
1962–2025, years charged by D4: premiums of PSA annual growth and of growth
relative to the mean of Indonesia, Malaysia and Thailand (World Bank), with the
shift test on each. H1b is supported if the dispersion of premiums (the
year-weighted standard deviation of P_a across administrations) of
peer-relative growth is less than half that of raw annual growth.

**RQ2 (luck).** Shocks (D12): oil = Hamilton net increase on WPU0561; US =
US growth purged of Philippine growth (residual on a constant, 4 own lags and
current + 4 lags of y); El Niño = max(0, ONI) quarterly mean; EBP = excess
bond premium purged the same way. (a) One shock at a time (Table 6 analogue):
each administration's explained premium and s.e. (b) All four jointly (Table
10 analogue; sample 1983Q4–2026Q2, set by the purging and lags). (c) For each
administration, raw, explained and unexplained premium on the joint sample.
(d) Summary: the share of the dispersion of premiums explained by luck,
S = 1 − Σ_a n_a U_a² / Σ_a n_a P_a², where U_a is the unexplained premium. H2a
(about half, as in the US) is supported if 0.35 ≤ S ≤ 0.65; H2b (more than
half) if S > 0.65; neither if S < 0.35. S is descriptive; inference is carried
by each administration's explained premium and its s.e.

**RQ3 (inheritance).** For each administration that starts inside the sample
(C. Aquino to Marcos Jr.), forecasts of growth over its first four charged
quarters, 100·ln(GDP_{s+3}/GDP_{s−1}), made with data through the quarter
before it starts (s − 1), from (i) an AR model: four-quarter log growth on the
current and four lags of quarterly log growth (Blinder and Watson Table 5 note);
(ii) a bounce-back AR that adds the current and four lags of a recession
indicator R_t (1 if seasonally adjusted q/q growth < 0) and their interactions
with growth. Both are estimated on the full sample, as in the reference's Table
5 panels C–D. H3 is supported for an administration if the bounce-back forecast
exceeds the sample mean of four-quarter growth by at least half of the actual
first-year excess; it is judged for C. Aquino and Marcos Jr.

**RQ4 (current administration, descriptive).** With N = 15 (the Marcos Jr.
quarters observed), each administration's raw and luck-adjusted (y − ĉ, from the
joint model) average over its first N charged quarters, and its difference from
Marcos Jr. with an NW s.e. Marcos Sr. is excluded (his first quarters are
outside the sample).

**Objective 1 scorecard (descriptive).** Annual 1961–2025, years charged by
D4, Macapagal to Marcos Jr. (Marcos Jr. 2023–2025): PSA real GDP growth; World
Bank GDP per capita growth, CPI inflation, unemployment (ILO modelled,
1991–); peer-relative growth. Each as the administration mean and as a z-score,
z = (administration mean − 1961–2025 mean) / s.d. of the annual values. No
composite index and no ranking of presidents.

**Robustness** (for RQ1 raw premiums and the RQ2 joint model): (a) timing lags
0, 2 and 4 quarters; (b) excluding 2020Q2–2021Q1 (pandemic); (c) excluding
1984Q1–1985Q4 (debt crisis); (d) log growth (400·Δln) instead of compounded;
(e) lags 1–6; (f) foreign demand as the purged equal-weight average of US,
Japan and euro-area growth (sample from 1997); (g) Vietnam added to the peers
(annual, from 1985).

## Results (2026-10-16; `output/tables/`, all pre-registered unless labelled)

- **RQ1: H1a not supported; H1b rejected (the opposite holds).** Quarterly raw
  premiums, 1981Q2–2026Q2 (`rq1_premiums_q.csv`): Marcos Sr. (1981–86 only)
  −4.22 (s.e. 2.26, p = 0.06, Holm 0.44), C. Aquino −0.77 (1.38), Ramos −0.24
  (0.93), Estrada −0.54 (0.83), Arroyo +1.07 (0.70), Aquino III +2.22 (0.72;
  p = 0.002, Holm 0.017, the only one that survives), Duterte +0.70 (1.84),
  Marcos Jr. +0.56 (0.90, p = 0.53). Shift test p = 0.44 (per person 0.28):
  the spread of administration averages is what chance alone would give.
  Annual 1962–2025: shift test p = 1.00 (every other alignment of the calendar
  gives a larger spread; Marcos Sr.'s 20-year block averages boom and bust).
  Relative to Indonesia, Malaysia and Thailand the spread is 2.4 times *larger*,
  not smaller: Marcos Sr. −1.73, C. Aquino −3.26, Aquino III +2.90, Duterte
  +2.16, Marcos Jr. +2.37 (`rq1_premiums_a.csv`). The Philippines lagged its
  peers badly before 1992 and has outgrown them since 2011.
- **RQ2: S = 0.48 (H2a by the pre-set rule), but fragile.** Joint model
  1983Q4–2026Q2 (`rq2_joint.csv`, `rq2_summary.csv`). The shocks matter jointly
  (Wald p < 0.001); the excess bond premium is significant (p = 0.005), oil
  borderline (p = 0.09), US demand (p = 0.53, negative sum) and El Niño
  (p = 0.84) are not. Much of S comes from Marcos Sr.'s 11 crisis quarters,
  where the US term (US boom while the Philippines collapsed) "explains" −2.0
  points. S falls to 0.12 without 1984–85 and to 0.11 with the US–Japan–euro
  area composite; 0.33–0.40 with other timing lags (`robustness.csv`). Aquino
  III: premium 2.14, of which luck 1.04 (s.e. 0.78). Marcos Jr.: 0.49, luck
  0.33 (0.24), unexplained 0.16.
- **RQ3: H3 supported for C. Aquino and Marcos Jr.** (`rq3_inheritance.csv`).
  First-year growth against the bounce-back forecast made the quarter before
  taking office (sample mean 3.70): C. Aquino 4.51 vs 4.64; Marcos Jr. 5.75 vs
  4.88 (forecast excess 1.18 ≥ half the actual excess 2.05). Duterte's first
  year (7.14 vs 4.81) beat the forecast; Ramos (2.34 vs 1.05) also did.
- **RQ4 (descriptive).** First 15 quarters (`rq4_same_point.csv`), raw /
  luck-adjusted: Marcos Jr. 4.59 / 4.26; C. Aquino 5.17 / 5.14; Ramos 4.54 /
  3.64; Arroyo 5.09 / 4.60; Aquino III 6.02 / 4.29; Duterte 1.24 / 1.21 (his
  first 15 quarters end in 2020Q2). No difference from Marcos Jr. is larger
  than 1.5 standard errors.
- **Objective 1 (`scorecard.csv`).** Marcos Jr. 2023–25: growth 5.08% (z
  +0.28), per person 4.36% (+0.68), relative to peers +1.14 (+0.69), inflation
  3.62% (−0.58), unemployment 2.21% (−1.90, lowest since 1991 on the ILO
  modelled series).
- **Robustness:** the Aquino III raw premium stays between 1.83 and 2.77 in every
  check; Marcos Jr.'s stays between 0.18 and 0.83; the shift-test p never falls
  below 0.26.
- **Bug fix (not a specification change):** the first run of `05_estimate.py`
  cut the oil and El Niño series at 1981, so their single-shock models started
  in 1982Q3; fixed to the planned 1981Q2. The joint model was unaffected.

## Documents

- `docs/feasibility_note.md`: what can and cannot be done, and with what data
  (Phase 1).

## Pipeline

`scripts/01_download_*.py` (raw data) → `scripts/00_get_x13.sh` (X-13 binary
into `.tools/`, not committed) → `scripts/02_clean.py` (processed tables,
seasonal adjustment) → `scripts/03_build_panel.py` → `scripts/04_replicate.py` (gate) →
`scripts/05_estimate.py` (RQ1–RQ4, scorecard, robustness) → `scripts/06_figures.py`.
Documents (manuscript from templates) to come.
Estimator and helpers in `phadmin/`; simulation tests in `tests/` (11 pass).
`./run_all.sh` rebuilds everything from `data/raw/`.

## Open questions

- [ ] The AER version of the reference (2016) may update the sample or the
      numbers in the 2014 working paper. If the user can upload the AER PDF, the
      targets will be checked against it and any change logged.
- [ ] Typhoon damage: is a long official series available (NDRRMC, PAGASA,
      EM-DAT with a login)? Without one, typhoons are not among the luck shocks.
- [ ] Presidents' term dates come from a secondary source (Wikipedia, saved in
      `data/raw/wiki/`), because the Official Gazette blocks this container.
      The user should spot-check them against the Official Gazette.
- [ ] Target journal: to be chosen by the user.
