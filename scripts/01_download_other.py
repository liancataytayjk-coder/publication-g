"""Download NOAA's Oceanic Nino Index and the IMF IFS Philippine quarterly GDP (cross-check), unchanged."""
from _raw import fetch

fetch("https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt", "data/raw/noaa/oni_ascii.txt.gz")
for key in ["NGDP_R_NSA_XDC", "NGDP_R_SA_XDC"]:
    fetch(f"https://api.db.nomics.world/v22/series/IMF/IFS/Q.PH.{key}?observations=1",
          f"data/raw/imf/ifs_q_ph_{key.lower()}.json.gz")
# Gilchrist-Zakrajsek excess bond premium, monthly 1973- (Federal Reserve Board, FEDS Notes)
fetch("https://www.federalreserve.gov/econres/notes/feds-notes/ebp_csv.csv", "data/raw/frb/ebp_monthly.csv.gz")
