---
title: "Good policy or good luck? Philippine economic performance across presidential administrations"
author:
  - "Lian Cataytay[^aff]"
date: "Draft, {{ n.build_date }}"
abstract: |
  Does the Philippine economy grow faster under some presidents than
  under others, and how much of the difference is luck? We replicate the design
  of Blinder and Watson (2016) on Philippine data. We first reproduce their US
  results on the paper's own data vintage (a 1.80-point growth gap between
  parties; ours is {{ n.gate_gap }}). We then measure each administration's
  *premium*, its average growth minus the 1981–2026 average, from quarterly data
  on {{ n.n_q }} quarters. We split the premium into the part explained by shocks
  no Philippine president controls (oil prices, demand from the United States, El
  Niño and world financial conditions) and the rest. Three findings stand out.
  First, the spread of administration premiums is no larger than chance would
  produce (randomization p = {{ n.shift_raw }}); only the Aquino III premium
  ({{ n.p_aquino_b }} points) survives a correction for multiple testing.
  Second, measured against Indonesia, Malaysia and Thailand, the differences grow
  rather than shrink: the Philippines lagged its neighbours before 1992 and has
  outgrown them since 2011. Third, luck explains about half of the spread of
  premiums ({{ n.S }}), as in the United States, but this share is fragile: it
  falls to {{ n.S_ex_debt }} without the 1984–85 debt crisis. The current
  administration's premium ({{ n.p_marcos_jr }}) is small and statistically
  indistinguishable from zero, and its strong first year was largely predictable
  from the rebound under way when it took office.

  **Keywords:** presidents, economic growth, luck, Philippines, replication

  **JEL codes:** E32, E60, O53
---

[^aff]: University of Southeastern Philippines. E-mail: lrcataytay00745\@usep.edu.ph.

<#-- Rendered by scripts/08_paper.py. Edit this template, never manuscript.md. --#>

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
constant 2018 prices, 1981Q1–{{ n.mj_last }}, which is not seasonally adjusted.
We remove the seasonal pattern with the US Census Bureau's X-13ARIMA-SEATS
program [@census2017x13]. Our adjusted growth correlates {{ n.sa_corr }} with
PSA's own adjusted series over the years PSA publishes it (2000–2026).

Growth is measured as in @blinder2016presidents, at a compounded annual rate:

$$y_t = 100\left[\left(\frac{GDP_t}{GDP_{t-1}}\right)^4 - 1\right]. \qquad\qquad (1)$$

For example, if real GDP rises by 1% in a quarter, $y_t = 100(1.01^4 - 1)
\approx 4.06$% a year. Over 1981Q2–{{ n.mj_last }}, growth averaged
{{ n.mean_q }}% a year.

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
The Marcos Jr. administration enters with the {{ n.mj_quarters }} quarters
observed so far (2022Q4–{{ n.mj_last }}).

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
model is estimated over {{ n.joint_sample }} ({{ n.joint_n }} quarters), the
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
compare every administration over its first {{ n.mj_quarters }} quarters, raw
and after removing the fitted shock component.

## Validation and pre-specification

Before touching Philippine data, we re-estimated the reference paper on US data
at its own data vintage (Table 1). The pass criteria were written down first.
The first run failed one criterion: both party averages were 0.13 points too
low, because we had used log growth instead of the compounded rate of equation
(1). With that correction, which we then applied to every growth rate, the
replication matches: Democratic mean {{ n.gate_d }} against 4.35, Republican
{{ n.gate_r }} against 2.54, gap {{ n.gate_gap }} against 1.80 (standard error
{{ n.gate_se }} against 0.64, randomization p = {{ n.gate_p }} against 0.01).
The oil shock explains {{ n.gate_oil }} of the gap, against 0.50 in the paper,
and its term-by-term effects correlate {{ n.gate_corr }} with the published ones
(Figure 6). The full Philippine estimation plan, including every hypothesis
test rule and robustness check, was then committed to the project's public
repository before the first Philippine estimate. All results below are from
that plan unless labelled otherwise. The estimation code was also checked on
simulated data with known answers.

# Results

## Do administrations differ?

Figure 1 shows quarterly growth with the administrations marked, and Table 2
the premiums. The largest negative premium belongs to the last five years of
Marcos Sr. ({{ n.p_marcos_sr }} points, s.e. {{ n.p_marcos_sr_se }}), the
years of the 1983–85 debt crisis. The largest positive premium belongs to
Aquino III ({{ n.p_aquino_b }}, s.e. {{ n.p_aquino_b_se }}, p =
{{ n.p_aquino_b_p }}); it is the only premium that survives the Holm correction
(p = {{ n.p_aquino_b_holm }}). The other premiums are within about one point of
zero, with standard errors of the same size. The Marcos Jr. premium so far is
{{ n.p_marcos_jr }} (s.e. {{ n.p_marcos_jr_se }}, p = {{ n.p_marcos_jr_p }}).

Taken together, the differences are no larger than chance alone would produce.
In the circular-shift test, {{ n.shift_raw }} of all alignments of the calendar
give a spread at least as large as the real one ({{ n.shift_pc }} for growth per
person). The first hypothesis, that differences are large and detectable as in
the United States (H1a), is therefore {{ n.h1a }}. Per person, the premiums of
recent administrations are larger because population growth has slowed; the
Marcos Jr. per-person premium is {{ n.pc_marcos_jr }} (s.e.
{{ n.pc_marcos_jr_se }}, p = {{ n.pc_marcos_jr_p }}, Holm p =
{{ n.pc_marcos_jr_holm }}).

The annual data tell the same story over six decades (Table 3): the shift-test
p-value is {{ n.shift_psa }}. Marcos Sr.'s twenty-year average contains both the
growth of the 1970s and the crash of 1984–85, and comes close to the long-run
mean ({{ n.pa_marcos_sr }} points).

Measured against regional peers, the picture changes (Figure 3). We expected
the peer comparison to remove much of the difference between administrations,
because the big swings of 1997–98, 2009 and 2020 were regional (H1b). The
opposite happens: the spread of peer-relative premiums is {{ n.disp_ratio }}
times the spread of raw premiums, so H1b is {{ n.h1b }}. Relative to its
neighbours, the Philippines grew much more slowly under Marcos Sr.
({{ n.rel_marcos_sr }} points) and C. Aquino ({{ n.rel_aquino_c }}), and faster
under Aquino III ({{ n.rel_aquino_b }}), Duterte ({{ n.rel_duterte }}) and Marcos
Jr. ({{ n.rel_marcos_jr }}). Much of this pattern comes from the peers
themselves: they grew {{ n.peers_pre97 }}% a year on average before 1997 and
{{ n.peers_post97 }}% since, while the Philippines grew {{ n.ph_pre97 }}% before
1997 and {{ n.ph_post10 }}% in 2011–2025. A peer-relative premium therefore mixes
the Philippines' record with its neighbours'. Even so, the shift test cannot reject
equal premiums on this measure either (p = {{ n.shift_rel }}).

## How much is luck?

Table 4 and Figure 2 split each premium into its explained and unexplained
parts. Jointly the shocks matter (p {{ n.wald_all }} for the test that all their
coefficients are zero), but not equally. World financial conditions are the
clearest: tighter credit markets abroad predict slower Philippine growth (p =
{{ n.wald_ebp }}). Oil prices matter at the 10% level (p = {{ n.wald_oil }}). US
demand (p = {{ n.wald_us }}) and El Niño (p = {{ n.wald_elnino }}) add little,
and the US-demand coefficients even sum to a negative number
({{ n.sum_us }}).

Luck explains a share S = {{ n.S }} of the spread of premiums, which by our
pre-set rule supports {{ n.h2 }}, the same order as in the United States. This
number should be read with care. Much of it comes from the 11 crisis quarters
of Marcos Sr. in the joint sample, where the model attributes
{{ n.j_marcos_sr_us }} points to US demand: the United States was booming in
1984 while the Philippines collapsed. That is an accident of timing, not a
plausible channel. Without 1984–85, S falls to {{ n.S_ex_debt }}; with a
broader measure of foreign demand (the United States, Japan and the euro area,
from 1997) it is {{ n.S_partners }}; with other timing conventions it ranges
from {{ n.S_lag_min }} to {{ n.S_lag_max }} (Table 7). We therefore do not
claim that luck explains half of the differences. We claim only that the
measured shocks explain a modest and uncertain share.

For individual administrations, luck explains about half of the Aquino III
premium ({{ n.j_aquino_b_E }} of {{ n.j_aquino_b_P }} points, s.e.
{{ n.j_aquino_b_Ese }}), mainly through oil prices ({{ n.j_aquino_b_oil }}) and
US demand ({{ n.j_aquino_b_us }}). For Marcos Jr., the premium on the joint sample is
{{ n.j_marcos_jr_P }} points, of which {{ n.j_marcos_jr_E }} (s.e.
{{ n.j_marcos_jr_Ese }}) is explained, mostly by easier world financial
conditions ({{ n.j_marcos_jr_ebp }}, partly offset by oil, {{ n.j_marcos_jr_oil }}),
leaving {{ n.j_marcos_jr_U }} unexplained. For Duterte the figures are
{{ n.j_duterte_P }}, {{ n.j_duterte_E }} and {{ n.j_duterte_U }}.

## Is early growth inherited?

Table 5 and Figure 4 compare first-year growth with what the two models
predicted at the start of each term. The bounce-back model predicted strong
first years for both administrations that took over after a collapse. For C.
Aquino it predicted {{ n.r3_aquino_c_bb }}%, against {{ n.r3_aquino_c_act }}%
actual. For Marcos Jr. it predicted {{ n.r3_marcos_jr_bb }}%, against
{{ n.r3_marcos_jr_act }}% actual (the sample mean is {{ n.mean4q }}%). By our
pre-set rule, the third hypothesis is {{ n.h3_aquino_c }} for C. Aquino and
{{ n.h3_marcos_jr }} for Marcos Jr.: a large part of their strong first years
was already under way. Duterte's first year ({{ n.r3_duterte_act }}% against a
forecast of {{ n.r3_duterte_bb }}%) and Ramos's ({{ n.r3_ramos_act }}% against
{{ n.r3_ramos_bb }}%) beat the forecasts.

## The current administration in context

Table 6 and Figure 5 compare administrations over their first
{{ n.mj_quarters }} quarters. Marcos Jr. averaged {{ n.r4_marcos_jr_raw }}% a
year ({{ n.r4_marcos_jr_adj }}% after removing the fitted luck component). This
is within the range of C. Aquino ({{ n.r4_aquino_c_raw }}%), Ramos
({{ n.r4_ramos_raw }}%), Arroyo ({{ n.r4_arroyo_raw }}%) and Aquino III
({{ n.r4_aquino_b_raw }}%; {{ n.r4_aquino_b_adj }}% luck-adjusted). Duterte's
first {{ n.mj_quarters }} quarters ({{ n.r4_duterte_raw }}%) end with the
pandemic collapse of 2020Q2. No difference from Marcos Jr. exceeds
{{ n.r4_max_t }} standard errors.

The annual scorecard (Table 8) adds other measures. In 2023–2025, GDP growth
averaged {{ n.sc_mj_g_psa }}% (z = {{ n.sc_mj_g_psa_z }}), growth per person
{{ n.sc_mj_gpc_wb }}% ({{ n.sc_mj_gpc_wb_z }}), growth relative to peers
{{ n.sc_mj_g_rel }} points ({{ n.sc_mj_g_rel_z }}), inflation
{{ n.sc_mj_inflation }}% ({{ n.sc_mj_inflation_z }}) and unemployment
{{ n.sc_mj_unemployment }}% ({{ n.sc_mj_unemployment_z }}), the lowest
administration average on this series, which starts in 1991. A z-score expresses each
measure in "typical swings" from its long-run average: z = (administration mean
− long-run mean) / standard deviation of the annual values.

## Robustness

Table 7 repeats the main statistics under every check that was specified in
advance. The conclusion that differences are within chance holds throughout
(the shift-test p never falls below {{ n.shift_min }}). The Aquino III premium
stays between {{ n.rob_aquino_b_min }} and {{ n.rob_aquino_b_max }} points, and
the Marcos Jr. premium between {{ n.rob_marcos_jr_min }} and
{{ n.rob_marcos_jr_max }}. The luck share is the fragile result, as discussed in
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
(raw data files, code and a one-command rebuild of every number, table and
figure) is deposited at Zenodo, doi:[to be inserted on deposit].

**Use of AI tools.** The code, analysis and first draft were prepared with the
assistance of Claude Code (Anthropic). The author checked all results and is
responsible for the content.

# References {-}

::: {#refs}
:::

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Tables {-}

{{ t.gate }}

{{ t.rq1 }}

{{ t.rq1a }}

{{ t.rq2 }}

{{ t.rq3 }}

{{ t.rq4 }}

{{ t.rob }}

{{ t.score }}

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Figures {-}

![Figure 1. Quarterly real GDP growth, 1981Q2–{{ n.mj_last }}, at a compounded annual rate (percent). Shading marks alternating administrations, with quarters charged after a one-quarter lag. The dashed line is the sample mean. The 2020Q2 value is cut at −30 for readability.](fig1_growth_by_admin.png){width=100%}

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

![Figure 2. Each administration's premium (average growth minus the sample mean, percentage points), the part explained by the four luck shocks (with a 95% confidence interval) and the unexplained rest, joint model {{ n.joint_sample }}.](fig2_premiums_luck.png){width=100%}

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

![Figure 5. Average growth over each administration's first {{ n.mj_quarters }} quarters, raw (filled circles) and after removing the fitted luck component (open squares), percent at an annual rate.](fig5_same_point.png){width=90%}

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

![Figure 6. Replication: the effect of oil shocks on average growth in each US presidential term, from Table 7 of Blinder and Watson (horizontal axis) and from this study (vertical axis). The dotted line is the 45-degree line.](fig6_replication.png){width=55%}
