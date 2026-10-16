# Raw data source log

One row per file in `data/raw/`. Files are saved exactly as downloaded (gzipped).

| File | Source / URL | Date pulled | Base / units | Coverage | Notes |
| --- | --- | --- | --- | --- | --- |
| `wiki/list_of_presidents_of_the_philippines_20261016.html.gz` | https://en.wikipedia.org/wiki/List_of_presidents_of_the_Philippines | 2026-10-16 | HTML page | Presidents 1899–2026 | Secondary source for term dates in `data/manual/administrations.csv`; the Official Gazette (officialgazette.gov.ph) returned 403 from this container. To be spot-checked by the user. |

## Planned (Phase 2)

| Series | Source | Checked reachable 2026-10-16 |
| --- | --- | --- |
| Philippines real GDP, quarterly, NSA and SA | IMF IFS via DBnomics (`IMF/IFS/Q.PH.NGDP_R_NSA_XDC`, `..._SA_XDC`) | yes: NSA 1981Q1–2024Q3, SA 2000Q1–2024Q3 |
| Philippines real GDP after 2024Q3 | PSA OpenSTAT / national accounts | no (403); ask user |
| GDP, GDP per capita, inflation, PH and peers, annual | World Bank WDI API | yes: 1960–2025 |
| US real GDP at 2014-07-01 vintage | ALFRED `GDPC1` | yes |
| PPI crude petroleum | FRED `WPU0561` | yes: 1947-01–2026-09 |
| Oceanic Niño Index | NOAA CPC `oni.ascii.txt` | yes |
| Brent, Dubai, WTI crude | FRED `POILBREUSDQ`, `POILDUBUSDM`, `MCOILWTICO` | yes: from 1992, 1992, 1986 |
