---
title: "Good policy or good luck? Philippine economic performance across presidential administrations"
author:
  - "Lian Cataytay[^aff]"
date: "Draft, 16 October 2026"
abstract: |
  Does the Philippine economy grow faster under some presidents than
  under others, and how much of the difference is luck? We replicate the design
  of Blinder and Watson (2016) on Philippine data. We first reproduce their US
  results on the paper's own data vintage (a 1.80-point growth gap between
  parties; ours is 1.80). We then measure each administration's
  *premium*, its average growth minus the 1981–2026 average, from quarterly data
  on 181 quarters. We split the premium into the part explained by shocks
  no Philippine president controls (oil prices, demand from the United States, El
  Niño and world financial conditions) and the rest. Three findings stand out.
  First, the spread of administration premiums is no larger than chance would
  produce (randomization p = 0.44); only the Aquino III premium
  (+2.22 points) survives a correction for multiple testing.
  Second, measured against Indonesia, Malaysia and Thailand, the differences grow
  rather than shrink: the Philippines lagged its neighbours before 1992 and has
  outgrown them since 2011. Third, luck explains about half of the spread of
  premiums (0.48), as in the United States, but this share is fragile: it
  falls to 0.12 without the 1984–85 debt crisis. The current
  administration's premium (+0.56) is small and statistically
  indistinguishable from zero, and its strong first year was largely predictable
  from the rebound under way when it took office.

  **Keywords:** presidents, economic growth, luck, Philippines, replication

  **JEL codes:** E32, E60, O53
---

[^aff]: University of Southeastern Philippines. E-mail: lrcataytay00745\@usep.edu.ph.



# Introduction

Every Philippine administration claims credit for growth, and every opposition
blames the president for slowdowns. Both claims assume that presidents move the
growth rate. Yet the largest swings in Philippine growth since 1981 came with
events that no president chose: the oil shocks, the 1997–98 Asian financial
crisis, the 2008–09 world recession and the 2020 pandemic. A president who
governs in calm years looks good; one who governs through a world recession
looks bad, whatever either did.

This paper asks two questions. Did the Philippine economy grow faster under some
presidents than others? And how much of the difference is luck, meaning shocks
from outside that no Philippine president controls? We follow
@blinder2016presidents, who asked the same questions for the United States.
They found that the US economy grew 1.8 percentage points a year faster under
Democratic than under Republican presidents, and that oil prices, productivity,
wars and growth abroad explain about half of that gap. Their design transfers to
the Philippines with one change. The Philippines has no stable two-party system:
the nine presidents since 1961 came from seven parties, and no party held the
presidency twice in a row. We therefore compare administrations one by one.

The paper makes three contributions. It provides the first estimate, to our
knowledge, of how much of the differences in growth between Philippine
administrations is luck, using the method of @blinder2016presidents after
reproducing their US results to two decimals. It puts six decades of
administrations on a common footing, per person and relative to regional peers.
And it gives an evidence-based reading of the current administration's record
at the same point in the term as its predecessors. Earlier accounts of
Philippine growth by period, such as @balisacan2003philippine and
@clarete2018philippine, are narrative; the political-cycle literature
[@alesina1997cycles] concerns advanced democracies with stable parties.

All specification choices were written down and time-stamped before the first
Philippine estimate (Section 2.6). The study measures; it does not rank people.
Every claim about an administration is tied to a number and its uncertainty,
and the luck-adjusted figure is always shown next to the raw one.

# Data and methods

## Data

The main measure is quarterly real GDP growth. Real GDP is the value of
everything the economy produces, at constant prices, so that inflation does not
count as growth. We use the Philippine Statistics Authority's (PSA) series at
constant 2018 prices, 1981Q1–2026Q2, which is not seasonally adjusted.
We remove the seasonal pattern with the US Census Bureau's X-13ARIMA-SEATS
program [@census2017x13]. Our adjusted growth correlates 0.978 with
PSA's own adjusted series over the years PSA publishes it (2000–2026).

Growth is measured as in @blinder2016presidents, at a compounded annual rate:

$$y_t = 100\left[\left(\frac{GDP_t}{GDP_{t-1}}\right)^4 - 1\right]. \qquad\qquad (1)$$

For example, if real GDP rises by 1% in a quarter, $y_t = 100(1.01^4 - 1)
\approx 4.06$% a year. Over 1981Q2–2026Q2, growth averaged
4.02% a year.

For the long view we use PSA's annual real GDP (1946–2025) and World Bank data
on GDP per person, inflation, unemployment and population, and on GDP growth in
Indonesia, Malaysia and Thailand (and Vietnam from 1985), 1961–2025. Presidents'
term dates come from the official record as compiled on Wikipedia (the Official
Gazette could not be reached from our computing environment). Every raw file,
with its source and date, is listed in the replication package.

## Charging quarters to administrations

A new president cannot change the economy on inauguration day. Following
@blinder2016presidents, who charge the first quarter of each term to the
previous president, we charge each quarter to the president who held office for
most of the *previous* quarter. For the 30 June inaugurations of 1992–2022 this
means a new president is charged from the October quarter. Corazon Aquino, who
took office on 25 February 1986, is charged from 1986Q3, and Gloria Macapagal
Arroyo, who took office on 20 January 2001, from 2001Q2. Years are charged to
the president who holds most of their quarters. Lags of zero, two and four
quarters are robustness checks. The quarterly data cover only the last five
years of Ferdinand E. Marcos (1981Q2–1986Q2), which we label "Marcos Sr.
(1981–86)". His whole presidency (1966–1985) enters the annual analysis.
The Marcos Jr. administration enters with the 15 quarters
observed so far (2022Q4–2026Q2).

## The administration premium

An administration's **premium** is its average growth minus the average over
the whole sample:

$$P_a = \bar{y}_a - \bar{y}. \qquad\qquad (2)$$

If growth averaged 4.0% over the sample and 5.0% under one administration, its
premium is +1.0 point. Standard errors, which measure how uncertain each
premium is, allow for correlation over time [Newey–West with six lags;
@newey1987hac]. Because there are only eight administrations in the quarterly
sample, we also use a test that does not rely on large-sample theory. The
**circular-shift test** slides the calendar of administrations along the growth
series by every possible number of quarters, keeping each administration's
length and the order of terms, and asks how often an arbitrary alignment gives
a larger spread of administration averages than the real one. Its p-value is
that share. It is the analogue of the random relabelling of terms in
@blinder2016presidents. When we test the eight premiums one by one, we also
report p-values corrected for multiple testing (Holm).

Two standardized versions put decades on a common footing. **Growth per
person** subtracts population growth. **Growth relative to peers** subtracts the
average growth of Indonesia, Malaysia and Thailand in the same year; it removes
shocks that hit the whole region at once.

## How much is luck?

We estimate the Philippine version of equation (1) in @blinder2016presidents:

$$y_t = \sum_a \alpha_a A_{a,t} + \sum_k \sum_{j=0}^{6} \gamma_{kj}\, e_{k,t-j} + u_t, \qquad\qquad (3)$$

where $A_{a,t}$ equals 1 in the quarters charged to administration $a$, and
$e_{k,t}$ is shock $k$, entered with its current value and six lags, because
shocks take time to work. The fitted shock component
$\hat{c}_t = \sum_k\sum_j \hat\gamma_{kj} e_{k,t-j}$ is the growth the shocks
alone predict. The **explained premium** of administration $a$ is the average
of $\hat c_t$ in its quarters minus the sample average of $\hat c_t$; the
**unexplained premium** is the rest. The unexplained premium is the most that
policy could have contributed. It is an upper bound, not a measure of policy,
because it also contains any luck we fail to measure.

We use four shocks, fixed before estimation. **Oil** is the net oil price
increase of @hamilton2003oil, the percentage by which the oil price exceeds its
highest value of the previous three years (zero otherwise), computed from the
US producer price index for crude petroleum, exactly as in the reference paper.
**US demand** is US real GDP growth. The United States was the largest market
for Philippine exports over most of the sample. **El Niño** is the positive part
of the Oceanic Niño Index of the US National Oceanic and Atmospheric
Administration; El Niño years bring drought to Philippine farms. **Financial
conditions** is the excess bond premium of @gilchrist2012credit, a measure of
stress in world credit markets. As in the reference paper, the US-demand and
financial series are first purged of any feedback from Philippine growth: we
keep only the part that cannot be predicted from their own past and from
current and past Philippine growth. Domestic fiscal policy, the central bank's
policy rate, coups and the 2020 lockdown are *not* treated as luck. The joint
model is estimated over 1983Q4–2026Q2 (171 quarters), the
period over which every shock and its lags exist.

A single summary is the **share of the spread of premiums explained by luck**,

$$S = 1 - \frac{\sum_a n_a U_a^2}{\sum_a n_a P_a^2}, \qquad\qquad (4)$$

where $U_a$ is the unexplained premium and $n_a$ the number of quarters. If luck
explained every premium exactly, $S = 1$; if it explained none, $S = 0$.

## Inheritance and the same point in the term

Growth in a president's first year may simply continue, or rebound from, what
was under way before. For each administration that starts inside the sample we
forecast growth over its first four quarters with data up to the quarter before
it took office, using two models estimated on the full sample, as in Table 5 of
@blinder2016presidents. The first is an autoregression, which predicts growth
from its own recent past. The second, the **bounce-back** model, adds an
indicator of recession quarters and its interaction with growth, so that growth
can rebound faster after a slump. The current term is incomplete, so we also
compare every administration over its first 15 quarters, raw
and after removing the fitted shock component.

## Validation and pre-specification

Before touching Philippine data, we re-estimated the reference paper on US data
at its own data vintage (Table 1). The pass criteria were written down first.
The first run failed one criterion: both party averages were 0.13 points too
low, because we had used log growth instead of the compounded rate of equation
(1). With that correction, which we then applied to every growth rate, the
replication matches: Democratic mean 4.35 against 4.35, Republican
2.54 against 2.54, gap 1.80 against 1.80 (standard error
0.64 against 0.64, randomization p = 0.011 against 0.01).
The oil shock explains 0.48 of the gap, against 0.50 in the paper,
and its term-by-term effects correlate 0.996 with the published ones
(Figure 6). The full Philippine estimation plan, including every hypothesis
test rule and robustness check, was then committed to the project's public
repository before the first Philippine estimate. All results below are from
that plan unless labelled otherwise. The estimation code was also checked on
simulated data with known answers.

# Results

## Do administrations differ?

Figure 1 shows quarterly growth with the administrations marked, and Table 2
the premiums. The largest negative premium belongs to the last five years of
Marcos Sr. (−4.22 points, s.e. 2.26), the
years of the 1983–85 debt crisis. The largest positive premium belongs to
Aquino III (+2.22, s.e. 0.72, p =
0.002); it is the only premium that survives the Holm correction
(p = 0.02). The other premiums are within about one point of
zero, with standard errors of the same size. The Marcos Jr. premium so far is
+0.56 (s.e. 0.90, p = 0.53).

Taken together, the differences are no larger than chance alone would produce.
In the circular-shift test, 0.44 of all alignments of the calendar
give a spread at least as large as the real one (0.28 for growth per
person). The first hypothesis, that differences are large and detectable as in
the United States (H1a), is therefore not supported. Per person, the premiums of
recent administrations are larger because population growth has slowed; the
Marcos Jr. per-person premium is +1.99 (s.e.
0.88, p = 0.02, Holm p =
0.17).

The annual data tell the same story over six decades (Table 3): the shift-test
p-value is 1.00. Marcos Sr.'s twenty-year average contains both the
growth of the 1970s and the crash of 1984–85, and comes close to the long-run
mean (−0.46 points).

Measured against regional peers, the picture changes (Figure 3). We expected
the peer comparison to remove much of the difference between administrations,
because the big swings of 1997–98, 2009 and 2020 were regional (H1b). The
opposite happens: the spread of peer-relative premiums is 2.4
times the spread of raw premiums, so H1b is not supported. Relative to its
neighbours, the Philippines grew much more slowly under Marcos Sr.
(−1.73 points) and C. Aquino (−3.26), and faster
under Aquino III (+2.90), Duterte (+2.16) and Marcos
Jr. (+2.37). Much of this pattern comes from the peers
themselves: they grew 7.0% a year on average before 1997 and
3.8% since, while the Philippines grew 4.0% before
1997 and 5.1% in 2011–2025. A peer-relative premium therefore mixes
the Philippines' record with its neighbours'. Even so, the shift test cannot reject
equal premiums on this measure either (p = 0.77).

## How much is luck?

Table 4 and Figure 2 split each premium into its explained and unexplained
parts. Jointly the shocks matter (p < 0.001 for the test that all their
coefficients are zero), but not equally. World financial conditions are the
clearest: tighter credit markets abroad predict slower Philippine growth (p =
0.005). Oil prices matter at the 10% level (p = 0.09). US
demand (p = 0.53) and El Niño (p = 0.84) add little,
and the US-demand coefficients even sum to a negative number
(−1.01).

Luck explains a share S = 0.48 of the spread of premiums, which by our
pre-set rule supports H2a (about half), the same order as in the United States. This
number should be read with care. Much of it comes from the 11 crisis quarters
of Marcos Sr. in the joint sample, where the model attributes
−2.67 points to US demand: the United States was booming in
1984 while the Philippines collapsed. That is an accident of timing, not a
plausible channel. Without 1984–85, S falls to 0.12; with a
broader measure of foreign demand (the United States, Japan and the euro area,
from 1997) it is 0.11; with other timing conventions it ranges
from 0.33 to 0.40 (Table 7). We therefore do not
claim that luck explains half of the differences. We claim only that the
measured shocks explain a modest and uncertain share.

For individual administrations, luck explains about half of the Aquino III
premium (+1.04 of +2.14 points, s.e.
0.78), mainly through oil prices (+0.54) and
US demand (+0.32). For Marcos Jr., the premium on the joint sample is
+0.49 points, of which +0.33 (s.e.
0.24) is explained, mostly by easier world financial
conditions (+0.40, partly offset by oil, −0.13),
leaving +0.16 unexplained. For Duterte the figures are
+0.63, +0.45 and +0.17.

## Is early growth inherited?

Table 5 and Figure 4 compare first-year growth with what the two models
predicted at the start of each term. The bounce-back model predicted strong
first years for both administrations that took over after a collapse. For C.
Aquino it predicted 4.64%, against 4.51%
actual. For Marcos Jr. it predicted 4.88%, against
5.75% actual (the sample mean is 3.70%). By our
pre-set rule, the third hypothesis is supported for C. Aquino and
supported for Marcos Jr.: a large part of their strong first years
was already under way. Duterte's first year (7.14% against a
forecast of 4.81%) and Ramos's (2.34% against
1.05%) beat the forecasts.

## The current administration in context

Table 6 and Figure 5 compare administrations over their first
15 quarters. Marcos Jr. averaged 4.59% a
year (4.26% after removing the fitted luck component). This
is within the range of C. Aquino (5.17%), Ramos
(4.54%), Arroyo (5.09%) and Aquino III
(6.02%; 4.29% luck-adjusted). Duterte's
first 15 quarters (1.24%) end with the
pandemic collapse of 2020Q2. No difference from Marcos Jr. exceeds
1.4 standard errors.

The annual scorecard (Table 8) adds other measures. In 2023–2025, GDP growth
averaged 5.08% (z = +0.28), growth per person
4.36% (+0.68), growth relative to peers
1.14 points (+0.69), inflation
3.62% (−0.58) and unemployment
2.21% (−1.90), the lowest
administration average on this series, which starts in 1991. A z-score expresses each
measure in "typical swings" from its long-run average: z = (administration mean
− long-run mean) / standard deviation of the annual values.

## Robustness

Table 7 repeats the main statistics under every check that was specified in
advance. The conclusion that differences are within chance holds throughout
(the shift-test p never falls below 0.26). The Aquino III premium
stays between 1.83 and 2.77 points, and
the Marcos Jr. premium between 0.18 and
0.83. The luck share is the fragile result, as discussed in
Section 3.2.

# Discussion

**Findings.** Philippine growth has differed across administrations by less than
headline debates suggest. With one exception, the differences are within what
chance would produce, and the one robust exception (Aquino III) owes about half
of its premium to favourable oil prices and financial conditions. The sharpest
contrast is with the neighbours: the Philippines fell far behind Indonesia,
Malaysia and Thailand in the 1980s and has grown faster than them since 2011.
Unlike in the United States, we cannot say with confidence that luck explains
about half of the differences; the share depends on a few crisis quarters. The
current administration's growth so far is close to the long-run average, its
strong start was largely predictable, and its record is indistinguishable from
its predecessors' at the same point in the term.

**What this means for reading growth claims (Objective 3).** A quarter or a
year of fast growth says little about a president. A fair reading of any
administration's record should show three numbers together: the raw average,
the average after removing world shocks, and the comparison with the same
point in earlier terms, each with its uncertainty. Our tables provide these
for every administration since 1981 and can be updated each quarter.

**Limitations.** There are only eight administrations in the quarterly sample,
so every estimate is imprecise. The unexplained premium is not a measure of
policy: it contains unmeasured luck, such as typhoons (for which we found no
long official quarterly series), remittance flows and domestic political
shocks, and it cannot separate the president from Congress, the independent
central bank (since 1993) or past decisions. Quarterly data begin in 1981, so
the earlier administrations enter only the annual analysis, and the national
accounts of the Marcos years are themselves debated. The Marcos Jr. term is
incomplete.

**Conclusion.** Measured carefully, the growth record of Philippine presidents
is mostly a story of shared fortunes and wide uncertainty, not of large and
reliable differences between administrations.

# Declarations {-}

**Funding.** None; this is personal research.

**Conflicts of interest.** None.

**Data and code availability.** All data are public. The replication package
(raw files, code and a one-command rebuild) is available at [repository URL to
be inserted].

**Use of AI tools.** [Author to confirm against the journal's policy:] The code,
analysis and first draft were prepared with the assistance of Claude Code
(Anthropic). The author checked all results and is responsible for the content.

# References {-}

::: {#refs}
:::

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Tables {-}


| Criterion | Statistic | Paper | This study | Pass range | Pass |
|:----------------|:------------------------------------------------|:----------|----------:|:----------------|:----------|
| G1 | D mean growth | 4.35 | 4.346 | [4.25, 4.45] | yes |
| G1 | R mean growth | 2.54 | 2.543 | [2.44, 2.64] | yes |
| G1 | D–R gap | 1.80 | 1.803 | [1.7, 1.9] | yes |
| G2 | Newey–West (6) s.e. of gap | 0.64 | 0.637 | [0.54, 0.74] | yes |
| G2 | randomization p-value (16 blocks) | 0.01 | 0.011 | [0.0, 0.03] | yes |
| G3 | oil-explained gap, adopted reading: lags 0–6 | 0.50 | 0.481 | [0.4, 0.6] | yes |
| G4 | corr. of term oil effects with Table 7 | ≥ 0.90 | 0.996 | [0.9, 1.0] | yes |
| G4 | terms with the same sign (of 16) | ≥ 14 | 16 | [14, 16] | yes |

Table: Table 1. Replication of Blinder and Watson (2016) on US data, 1949Q2–2013Q1

::: {custom-style="Table Note"}
*Notes:* Pass ranges were fixed before the gate was run. Growth is quarterly real GDP growth at a compounded annual rate, ALFRED vintage of 1 July 2014.

*Source:* Blinder and Watson (2014, Tables 1, 6 and 7); author's calculations from ALFRED and BLS data.
:::


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

| Administration | Quarters charged (n) | Mean growth | Premium (s.e.) | Holm p | Per-person premium (s.e.) |
|:------------------------|:-------------------------|------------:|----------------------:|----------:|----------------------:|
| Marcos Sr. (1981–86) | 1981Q2–1986Q2 (21) | −0.20 | −4.22\* (2.26) | 0.44 | −5.03\*\* (2.30) |
| C. Aquino | 1986Q3–1992Q3 (25) | 3.25 | −0.77 (1.38) | 1.00 | −1.35 (1.37) |
| Ramos | 1992Q4–1998Q3 (24) | 3.78 | −0.24 (0.93) | 1.00 | −0.60 (0.98) |
| Estrada | 1998Q4–2001Q1 (10) | 3.48 | −0.54 (0.83) | 1.00 | −1.03 (0.86) |
| Arroyo | 2001Q2–2010Q3 (38) | 5.09 | +1.07 (0.70) | 0.76 | +1.13 (0.76) |
| Aquino III | 2010Q4–2016Q3 (24) | 6.24 | +2.22\*\*\* (0.72) | 0.02 | +2.43\*\*\* (0.79) |
| Duterte | 2016Q4–2022Q3 (24) | 4.72 | +0.70 (1.84) | 1.00 | +1.54 (1.87) |
| Marcos Jr. | 2022Q4–2026Q2 (15) | 4.59 | +0.56 (0.90) | 1.00 | +1.99\*\* (0.88) |

Table: Table 2. Administration premiums in quarterly real GDP growth, 1981Q2–2026Q2

::: {custom-style="Table Note"}
*Notes:* Growth at a compounded annual rate, percent; premium = administration mean minus the sample mean (4.02%). Newey–West standard errors (6 lags) in parentheses. \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01 (unadjusted). Holm p corrects for the eight tests. Circular-shift test of no differences: p = 0.44 (raw), 0.28 (per person).

*Source:* Author's calculations from Philippine Statistics Authority, World Bank, FRED/ALFRED, NOAA and Federal Reserve Board data.
:::


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

| Administration | Years | Premium, PSA growth | Premium relative to IDN–MYS–THA | Relative to IDN–MYS–THA–VNM |
|:----------------------|----------:|--------------:|--------------------:|------------------------:|
| Macapagal | 4 | +0.86 | +1.25 |  |
| Marcos Sr. | 20 | −0.46 | −1.73 | −8.25 |
| C. Aquino | 7 | −0.84 | −3.26 | −2.82 |
| Ramos | 6 | −0.63 | +0.40 | −0.71 |
| Estrada | 2 | −0.37 | +0.14 | −0.21 |
| Arroyo | 10 | +0.55 | +1.23 | +0.64 |
| Aquino III | 6 | +1.87 | +2.90 | +2.33 |
| Duterte | 6 | −0.55 | +2.16 | +1.26 |
| Marcos Jr. | 3 | +0.92 | +2.37 | +1.57 |

Table: Table 3. Annual premiums, raw and relative to regional peers, 1962–2025

::: {custom-style="Table Note"}
*Notes:* Percentage points. Years charged to the administration in office for most of the year after a one-quarter lag. Dispersion of premiums: 0.82 (raw), 1.99 (relative). Shift-test p: 1.00 (raw), 0.77 (relative). Vietnam data start in 1985, so the last column covers only 1985 for Marcos Sr.

*Source:* Author's calculations from Philippine Statistics Authority, World Bank, FRED/ALFRED, NOAA and Federal Reserve Board data.
:::


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

| Administration | Premium | Explained (s.e.) | Unexplained | Oil | US demand | El Niño | Financial |
|:------------------------|-------------:|----------------:|------------------:|----------:|------------:|----------:|----------------:|
| Marcos Sr. (1983–86) | −6.97 | −2.03 (1.63) | −4.95 | +0.59 | −2.67 | +0.04 | +0.00 |
| C. Aquino | −0.85 | −0.22 (0.48) | −0.62 | −0.06 | +0.32 | −0.13 | −0.36 |
| Ramos | −0.32 | +0.29 (0.24) | −0.61 | +0.28 | −0.45 | −0.10 | +0.56 |
| Estrada | −0.61 | −1.90 (1.17) | +1.29 | +0.32 | −1.03 | −0.05 | −1.15 |
| Arroyo | +1.00 | −0.02 (0.62) | +1.02 | −0.76 | +0.90 | +0.18 | −0.35 |
| Aquino III | +2.14 | +1.04 (0.78) | +1.10 | +0.54 | +0.32 | −0.01 | +0.19 |
| Duterte | +0.63 | +0.45 (0.29) | +0.17 | +0.11 | +0.01 | −0.07 | +0.40 |
| Marcos Jr. | +0.49 | +0.33 (0.24) | +0.16 | −0.13 | +0.03 | +0.04 | +0.40 |

Table: Table 4. How much of each premium is luck? Joint shock model, 1983Q4–2026Q2

::: {custom-style="Table Note"}
*Notes:* Percentage points. Quarters as in Table 2 from 1983Q4 (Marcos Sr.: 11). Explained = the administration's average of the fitted shock component minus its sample average; the last four columns split it by shock. Each shock enters with lags 0–6. Share of the dispersion of premiums explained, S = 0.48. Wald tests that a shock's lags are all zero: oil p = 0.09, US demand p = 0.53, El Niño p = 0.84, financial conditions p = 0.005.

*Source:* Author's calculations from Philippine Statistics Authority, World Bank, FRED/ALFRED, NOAA and Federal Reserve Board data.
:::


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

| Administration | Forecast made in | Actual first-year growth | AR forecast | Bounce-back forecast | Inherited (H3 rule) |
|:----------------------|:--------------|-----------------:|--------------:|------------------:|:----------------|
| C. Aquino | 1986Q2 | 4.51 | 4.31 | 4.64 | yes |
| Ramos | 1992Q3 | 2.34 | 3.01 | 1.05 | no |
| Estrada | 1998Q3 | 3.53 | 3.01 | 2.40 | no |
| Arroyo | 2001Q1 | 3.78 | 3.34 | 2.91 | no |
| Aquino III | 2010Q3 | 3.16 | 4.24 | 5.02 | no |
| Duterte | 2016Q3 | 7.14 | 4.24 | 4.81 | no |
| Marcos Jr. | 2022Q3 | 5.75 | 4.20 | 4.88 | yes |

Table: Table 5. Was first-year growth inherited?

::: {custom-style="Table Note"}
*Notes:* Growth over the first four charged quarters, 100·ln(GDP_s+3 / GDP_s−1), percent. Sample mean 3.70%. 'Inherited' if the bounce-back forecast exceeds the mean by at least half of the actual excess.

*Source:* Author's calculations from Philippine Statistics Authority, World Bank, FRED/ALFRED, NOAA and Federal Reserve Board data.
:::


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

| Administration | First 15 quarters | Raw mean | Difference (s.e.) | Luck-adjusted mean | Difference  (s.e.) |
|:----------------------|:-------------------|----------:|-----------------:|---------------------:|-----------------:|
| C. Aquino | 1986Q3–1990Q1 | 5.17 | −0.58 (1.48) | 5.14 | −0.88 (2.16) |
| Ramos | 1992Q4–1996Q2 | 4.54 | +0.05 (0.90) | 3.64 | +0.62 (1.38) |
| Arroyo | 2001Q2–2004Q4 | 5.09 | −0.50 (0.96) | 4.60 | −0.35 (1.41) |
| Aquino III | 2010Q4–2014Q2 | 6.02 | −1.43 (1.01) | 4.29 | −0.04 (1.42) |
| Duterte | 2016Q4–2020Q2 | 1.24 | +3.35 (4.79) | 1.21 | +3.05 (4.54) |
| Marcos Jr. | 2022Q4–2026Q2 | 4.59 |  | 4.26 |  |

Table: Table 6. The same point in the term: the first 15 quarters

::: {custom-style="Table Note"}
*Notes:* Percent, annual rate. Difference = Marcos Jr. minus the administration in the row. Luck-adjusted growth removes the fitted shock component of the joint model. Estrada (10 quarters) and Marcos Sr. (first quarters outside the sample) are not compared. Newey–West standard errors; the luck-adjusted ones ignore the estimation error of the shock component.

*Source:* Author's calculations from Philippine Statistics Authority, World Bank, FRED/ALFRED, NOAA and Federal Reserve Board data.
:::


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

| Specification | Shift-test p | Luck share S | Aquino III premium | Marcos Jr. premium |
|:---------------------------------------|-----------------:|----------:|-------------:|-------------:|
| Main | 0.44 | 0.48 | +2.22 | +0.56 |
| Timing lag 0 | 0.27 | 0.33 | +2.15 | +0.79 |
| Timing lag 2 | 0.34 | 0.40 | +2.32 | +0.35 |
| Timing lag 4 | 0.26 | 0.39 | +2.77 | +0.83 |
| Excluding 2020Q2–2021Q1 | 0.42 | 0.47 | +2.15 | +0.50 |
| Excluding 1984Q1–1985Q4 | 0.86 | 0.12 | +1.83 | +0.18 |
| Log growth | 0.43 | 0.43 | +2.35 | +0.77 |
| Lags 1–6 | 0.44 | 0.51 | +2.22 | +0.56 |
| Foreign demand US-JP-EA (from 1997) | 0.44 | 0.11 | +2.22 | +0.56 |

Table: Table 7. Robustness checks

::: {custom-style="Table Note"}
*Notes:* All checks were specified before estimation. Premiums are raw quarterly premiums (percentage points).

*Source:* Author's calculations from Philippine Statistics Authority, World Bank, FRED/ALFRED, NOAA and Federal Reserve Board data.
:::


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

| Administration | GDP growth | Growth per person | Relative to peers | Inflation | Unemployment (1991–) |
|:----------------------|----------------:|----------------:|-----------------:|-----------------:|--------------------:|
| Macapagal | 5.02 (+0.26) | 1.92 (−0.04) | 0.02 (+0.37) | 5.54 (−0.34) |  |
| Marcos Sr. | 3.70 (−0.14) | 1.16 (−0.26) | −2.97 (−0.51) | 14.32 (+0.74) |  |
| C. Aquino | 3.32 (−0.26) | 0.81 (−0.36) | −4.50 (−0.95) | 10.20 (+0.23) | 3.79 (+0.79) |
| Ramos | 3.53 (−0.19) | 1.24 (−0.24) | −0.84 (+0.12) | 7.71 (−0.07) | 3.70 (+0.64) |
| Estrada | 3.79 (−0.11) | 1.33 (−0.21) | −1.09 (+0.04) | 4.96 (−0.41) | 3.76 (+0.74) |
| Arroyo | 4.71 (+0.17) | 2.85 (+0.24) | −0.00 (+0.36) | 4.64 (−0.45) | 3.69 (+0.62) |
| Aquino III | 6.03 (+0.57) | 4.43 (+0.70) | 1.67 (+0.85) | 2.64 (−0.70) | 3.33 (+0.00) |
| Duterte | 3.61 (−0.17) | 2.74 (+0.20) | 0.93 (+0.63) | 3.78 (−0.56) | 2.61 (−1.23) |
| Marcos Jr. | 5.08 (+0.28) | 4.36 (+0.68) | 1.14 (+0.69) | 3.62 (−0.58) | 2.21 (−1.90) |

Table: Table 8. Scorecard, annual averages 1962–2025 (z-score in parentheses)

::: {custom-style="Table Note"}
*Notes:* Percent; z = (administration mean − 1962–2025 mean) / standard deviation of the annual values. For inflation and unemployment a negative z means a lower rate than usual. No composite index is formed and administrations are not ranked. Unemployment is the ILO modelled estimate (1991–).

*Source:* Author's calculations from Philippine Statistics Authority, World Bank, FRED/ALFRED, NOAA and Federal Reserve Board data.
:::


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Figures {-}

![Figure 1. Quarterly real GDP growth, 1981Q2–2026Q2, at a compounded annual rate (percent). Shading marks alternating administrations, with quarters charged after a one-quarter lag. The dashed line is the sample mean. The 2020Q2 value is cut at −30 for readability.](fig1_growth_by_admin.png){width=100%}

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

![Figure 2. Each administration's premium (average growth minus the sample mean, percentage points), the part explained by the four luck shocks (with a 95% confidence interval) and the unexplained rest, joint model 1983Q4–2026Q2.](fig2_premiums_luck.png){width=100%}

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

![Figure 3. Annual premiums, 1962–2025: Philippine growth (white) and Philippine growth minus the average of Indonesia, Malaysia and Thailand (grey), percentage points.](fig3_peers.png){width=100%}

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

![Figure 4. Growth over each administration's first four quarters (bars) against forecasts made in the quarter before it took office: an autoregression (circles) and a bounce-back model (squares). The dashed line is the sample mean.](fig4_inheritance.png){width=100%}

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

![Figure 5. Average growth over each administration's first 15 quarters, raw (filled circles) and after removing the fitted luck component (open squares), percent at an annual rate.](fig5_same_point.png){width=90%}

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

![Figure 6. Replication: the effect of oil shocks on average growth in each US presidential term, from Table 7 of Blinder and Watson (horizontal axis) and from this study (vertical axis). The dotted line is the 45-degree line.](fig6_replication.png){width=55%}
