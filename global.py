
import requests
import pandas as pd

src = {
    "Globe": "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv",
    "North": "https://data.giss.nasa.gov/gistemp/tabledata_v4/NH.Ts+dSST.csv",
    "South": "https://data.giss.nasa.gov/gistemp/tabledata_v4/SH.Ts+dSST.csv"
}

# ---- Download files ----
for region, url in src.items():
    r = requests.get(url)
    r.raise_for_status()
    with open(f"{region}.csv", "wb") as f:
        f.write(r.content)

# ---- Function to read and reshape each file ----
def read_temp(region):
    # Skip 1 line, read first 13 columns, *** -> NaN
    df = pd.read_csv(
        f"{region}.csv",
        skiprows=1,
        usecols=range(13),
        na_values="***"
    )
    # Pivot longer: columns Jan..Dec → rows
    df = df.melt(
        id_vars="Year",
        var_name="Month",
        value_name="AvTemp"
    )
    df["Date"] = pd.to_datetime(df["Year"].astype(str) + " " + df["Month"],
                                format="%Y %b")
    df["Region"] = region
    df = df.dropna(subset=["AvTemp"])
    return df


data = pd.concat([read_temp("Globe"), read_temp("North"), read_temp("South")])
data.to_csv("global-temp.csv", index=False)

