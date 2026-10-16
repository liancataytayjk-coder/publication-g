# Feasibility note: presidents and the Philippine economy

*Phase 1, 16 October 2026. Written before any Philippine estimate.*

## The question, and the version of it that can be answered

The question that started this study is whether the economy is doing well under
the current administration, and more generally which administration "made the
economy good, and by how much". Put that way, the question cannot be answered
by comparing averages. Every president inherits an economy that is already
growing or shrinking. Policies take years to work, so a good reform can pay off
under the next president. And the biggest swings in Philippine growth came from
outside: the world oil shocks, the 1997–98 Asian financial crisis, the 2008–09
global recession and the 2020 pandemic. A president who happens to govern in
calm years looks good, and one who governs through a world recession looks bad,
whatever either of them did.

The version that can be answered is: **how much of the difference between
administrations is left after we remove the luck?** Blinder and Watson (2016)
asked exactly this for the United States. They found that the US economy grew
1.8 percentage points a year faster under Democratic presidents than under
Republican ones, and that oil prices, productivity, wars and growth abroad
explain about half of that gap. Their method transfers to the Philippines with
one change: the Philippines has no stable two-party system, so we compare
administrations one by one instead of parties.

## What we will measure

The main measure is quarterly real GDP growth at an annual rate. Real GDP is the
value of everything the economy produces in a year, at constant prices, so that
inflation does not count as growth. Quarterly growth at an annual rate is
g_t = 400 × ln(GDP_t / GDP_{t−1}). For example, if real GDP rises by 1.5% in a
quarter, the annual rate is about 6%.

Each administration's **premium** is its average growth minus the average over
the whole period: P_a = ḡ_a − ḡ. If growth averaged 4.0% over 1981–2026 and
5.0% under one president, that administration's premium is +1.0 point.

We then split each premium into two parts. The **explained premium** is the part
predicted by shocks that no Philippine president controls: the world price of
oil, growth in the countries that buy Philippine exports, El Niño droughts, and
world financial conditions. The **unexplained premium** is the rest. It is the
most that policy could have contributed. It is an upper bound, not a measure of
policy, because it also contains any luck we fail to measure.

## Putting decades on a common footing

Comparing 1966 with 2024 needs a common yardstick. We use three. First, growth
per person, which removes the effect of faster population growth in earlier
decades. Second, growth relative to regional peers (Indonesia, Malaysia and
Thailand), which removes shocks that hit the whole region at once. For example,
if the Philippines grew 3% in a year when its peers grew 4%, its relative growth
is −1 point. Third, z-scores, which express each measure in "typical swings"
from its long-run average: z = (x − mean) / standard deviation. A growth
z-score of +1 means one typical swing better than usual, and it lets growth,
inflation and unemployment be read on one scale.

## Data: what is available

Quarterly real GDP for the Philippines from 1981Q1 to 2024Q3 is available from
the IMF's International Financial Statistics, a copy of the official PSA series.
The years after 2024Q3 must come from the Philippine Statistics Authority
(PSA), whose website blocks this computer; we will ask you for that file or for
wider network access. Annual GDP, GDP per person and inflation from 1960 to 2025,
for the Philippines and its peers, come from the World Bank. The oil price
series the reference paper uses (the US producer price index for crude
petroleum) runs from 1947 to 2026 on FRED, the St Louis Fed database. El Niño
is measured by the US National Oceanic and Atmospheric Administration's Oceanic
Niño Index, from 1950. US GDP at the exact data vintage the reference paper used
(July 2014) is on ALFRED, the archival version of FRED, which lets us reproduce
the paper's numbers before touching Philippine data.

## What cannot be done, and the substitutes

Quarterly data begin in 1981, so the main analysis sees only the last five years
of Marcos Sr. (1981–86), which were the years of the debt crisis. His whole
presidency (1966–86) enters only the annual long view, 1961–2025, where fewer
shocks are measured. Typhoon damage is an obvious source of luck, but we have not
found a long official quarterly series; unless you can supply one, typhoons are
left out and we say so. The current administration's term is incomplete, so we
also compare every administration at the same point in its term: its first N
quarters, where N is the number of Marcos Jr. quarters observed so far.

## Limits that will remain

There are only eight to nine administrations, so differences between them are
estimated with wide uncertainty, and the study will say so in every table. We
cannot separate the president from Congress, from the Bangko Sentral ng
Pilipinas (independent since 1993) or from what each administration inherited.
Unemployment and poverty definitions changed over time (for example the 2005
change in the unemployment definition), so they appear only in the descriptive
scorecard, with breaks flagged. The study can show how much of the gap between
administrations is luck. It cannot name a "best president", and it will not try
to.

## Next steps

Phase 2 downloads and logs every series, fixes the luck shocks and checks our
seasonal adjustment against the IMF's. Phase 3 reproduces Blinder and Watson's
US results against the pass criteria written in `CLAUDE.md` before any run.
Only then do we estimate anything for the Philippines.
