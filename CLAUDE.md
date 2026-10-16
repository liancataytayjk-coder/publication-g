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

**Result:** not yet run.

## Estimation plan

To be written in full, and dated, after Phase 2 fixes the shock series and
before the first Philippine estimate. It will cover: RQ1 means, standard errors
and the shift test, on raw, per-person and peer-relative growth; RQ2 one shock
at a time and jointly (as in Tables 6 and 10), with each administration's
explained and unexplained premium (as in Table 7); RQ3 first-year forecasts
(AR(4), bounce-back AR); RQ4 the same-point-in-term comparison; and robustness:
timing lags 0/2/4, excluding 2020Q2–2021Q1, excluding the 1984–85 crisis,
annual long sample, and Vietnam in the peer group.

## Results

None yet.

## Documents

- `docs/feasibility_note.md`: what can and cannot be done, and with what data
  (Phase 1).

## Pipeline

Not yet built. `./run_all.sh` will rebuild everything from `data/raw/`.

## Open questions

- [ ] The AER version of the reference (2016) may update the sample or the
      numbers in the 2014 working paper. If the user can upload the AER PDF, the
      targets will be checked against it and any change logged.
- [ ] Philippine quarterly GDP after 2024Q3: PSA OpenSTAT is blocked here. Can
      the user download PSA's quarterly national accounts (constant 2018
      prices, 1981 onwards if available), or widen network access to
      `openstat.psa.gov.ph`?
- [ ] Typhoon damage: is a long official series available (NDRRMC, PAGASA,
      EM-DAT with a login)? Without one, typhoons are not among the luck shocks.
- [ ] Presidents' term dates come from a secondary source (Wikipedia, saved in
      `data/raw/wiki/`), because the Official Gazette blocks this container.
      The user should spot-check them against the Official Gazette.
- [ ] Target journal: to be chosen by the user.
- [ ] The `lian-signature-style` output skill is not available in this session
      (not found in the skill list on 2026-10-16). The user to re-install or
      paste its rules; until then the empirical-econ-study style guide applies.
