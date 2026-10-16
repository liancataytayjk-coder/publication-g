"""Download World Bank WDI indicators (annual) for the Philippines and its peers, unchanged JSON.

Peers (D8, approved by the user 2026-10-16): Indonesia, Malaysia, Thailand;
Vietnam for robustness.
"""
from _raw import fetch

COUNTRIES = "PHL;IDN;MYS;THA;VNM"
INDICATORS = {
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    "NY.GDP.MKTP.KD": "gdp_const2015usd",
    "NY.GDP.PCAP.KD": "gdppc_const2015usd",
    "NY.GDP.PCAP.KD.ZG": "gdppc_growth",
    "FP.CPI.TOTL.ZG": "cpi_inflation",
    "SL.UEM.TOTL.ZS": "unemployment_ilo_modeled",
    "SP.POP.TOTL": "population",
}
URL = "https://api.worldbank.org/v2/country/{}/indicator/{}?format=json&per_page=2000&date=1960:2026"

for code, name in INDICATORS.items():
    fetch(URL.format(COUNTRIES, code), f"data/raw/worldbank/wdi_{name}_5countries.json.gz")
