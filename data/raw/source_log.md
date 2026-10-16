# Raw data source log

One row per file in `data/raw/`. Files are saved exactly as downloaded
(gzipped). All files below were pulled on 2026-10-16 by the `scripts/01_download_*.py`
script named in the last column.

| File | Source / URL | Base / units | Coverage | Notes | Script |
| --- | --- | --- | --- | --- | --- |
| `wiki/list_of_presidents_of_the_philippines_20261016.html.gz` | https://en.wikipedia.org/wiki/List_of_presidents_of_the_Philippines | HTML page | Presidents 1899–2026 | Secondary source for `data/manual/administrations.csv`; the Official Gazette returned 403. To be spot-checked by the user. | manual (curl) |
| `psa/gdp_q_byexpenditure_1981_latest.csv.gz` | PSA OpenSTAT `DB/2B/NA/QT/23QNAP/EXP/0952B5BQEQ1.px` | PHP million, current and constant 2018 prices, not seasonally adjusted | 1981Q1–2026Q2 (2026Q3–Q4 columns empty) | Main outcome series (D10). Identical to the current table over 2000Q1–2026Q2 (ratio 1.000000). | `01_download_psa.py` |
| `psa/gni_gdp_q_byexpenditure_2000_latest.csv.gz` | PSA OpenSTAT `DB/2B/NA/QT/1SUM/0012B5BEXQ1.px` | PHP million, current and constant 2018 prices, NSA | 2000Q1–2026Q2 | Current release (updated 2026-08-07); used to check the long series. | `01_download_psa.py` |
| `psa/gni_gdp_q_sa_byexpenditure_2000_latest.csv.gz` | PSA OpenSTAT `DB/2B/SANA/1SUM/012B5BEXS1.px` | PHP million, constant 2018 prices, seasonally adjusted by PSA | 2000Q1–2026Q2 | Benchmark for our own seasonal adjustment (D10). | `01_download_psa.py` |
| `psa/gdp_a_byindustry_1946_latest.csv.gz` | PSA OpenSTAT `DB/2B/NA/AN/23ANAP/0942B5BANA1.px` | PHP million, current and constant 2018 prices | 1946–2025 | Annual GDP for the long view. | `01_download_psa.py` |
| `psa/percapita_gdp_gni_hfce_a.csv.gz` | PSA OpenSTAT `DB/2B/NA/AN/1SUM/0122B5BPCA1.px` | PHP per person, current and constant 2018 prices | 2000–2025 | Per-person check on the World Bank series. | `01_download_psa.py` |
| `fred/gdpc1_vintage20140701.csv.gz` | ALFRED `GDPC1`, vintage 2014-07-01 | US$ billion, chained 2009, SAAR | 1947Q1–2014Q1 | Replication gate (D9). | `01_download_fred.py` |
| `fred/gdpc1.csv.gz` | FRED `GDPC1` | US$ billion, chained 2017, SAAR | 1947Q1–2026Q2 | Foreign-demand shock (D12). | `01_download_fred.py` |
| `fred/wpu0561.csv.gz` | FRED `WPU0561` (BLS PPI, crude petroleum, domestic production) | index 1982=100, monthly, NSA | 1947-01–2026-09 | Hamilton oil shock, as in the reference. | `01_download_fred.py` |
| `fred/mcoilwtico.csv.gz`, `fred/poildubusdm.csv.gz`, `fred/poilbreusdq.csv.gz` | FRED WTI (EIA), Dubai and Brent (IMF) | US$ per barrel | 1986-01–2026-09; 1992-01–2026-07; 1992Q1–2026Q2 | Oil robustness. | `01_download_fred.py` |
| `fred/jpnrgdpexp.csv.gz`, `fred/clvmnacscab1gqea19.csv.gz` | FRED Japan real GDP; euro-area real GDP (Eurostat) | national currency, constant prices, SA | 1994Q1–2026Q2; 1995Q1–2026Q2 | Trading-partner composite (robustness, D12). | `01_download_fred.py` |
| `fred/usrec.csv.gz` | FRED `USREC` (NBER recession indicator) | 0/1, monthly | 1854-12–2026-09 | Context only. | `01_download_fred.py` |
| `worldbank/wdi_<indicator>_5countries.json.gz` (7 files) | World Bank WDI API, indicators NY.GDP.MKTP.KD.ZG, NY.GDP.MKTP.KD, NY.GDP.PCAP.KD, NY.GDP.PCAP.KD.ZG, FP.CPI.TOTL.ZG, SL.UEM.TOTL.ZS, SP.POP.TOTL | %, constant 2015 US$, persons | PHL, IDN, MYS, THA 1960/61–2025; VNM from 1984–96 (varies) | Peers and the scorecard (D8, D11). Unemployment is the ILO modelled estimate, 1991–. | `01_download_worldbank.py` |
| `noaa/oni_ascii.txt.gz` | NOAA CPC Oceanic Niño Index | °C, 3-month running means | DJF 1950–JAS 2026 | El Niño shock (D6). | `01_download_other.py` |
| `imf/ifs_q_ph_ngdp_r_nsa_xdc.json.gz`, `imf/ifs_q_ph_ngdp_r_sa_xdc.json.gz` | IMF IFS via DBnomics | PHP million, real | 1981Q1–2024Q3; 2000Q1–2024Q3 | Cross-check only: year-on-year growth equals PSA's to within 0.14 points. | `01_download_other.py` |
| `frb/ebp_monthly.csv.gz` | Federal Reserve Board, Gilchrist–Zakrajšek excess bond premium (FEDS Notes csv) | percentage points, monthly | 1973-01–2026-09 | Global financial-conditions shock (D12). | `01_download_other.py` |
