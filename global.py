import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

def read_temp(url, region):
    # read_csv: skip 3 rows, select columns (Date, Value)
    df = pd.read_csv(url, skiprows=3)
    # mutate equivalent
    df['Region'] = region
    df = df.rename(columns={'Anomaly' : 'AvTemp'})
    df['Date'] = pd.to_datetime(df['Date'].astype(str) + "01", format="%Y%m%d")
    return df

# Define areas
area_map = {
    "Globe": "globe",
    "North": "nhem",
    "South": "shem"
}

last_month = datetime.now() - relativedelta(months=1)
yr = last_month.strftime("%Y")

# Build the dataframes (equivalent to imap_dfr)
dfs = []
for name, code in area_map.items():
    url = f"https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/{code}/land_ocean/tavg/1/0/1850-{yr}/data.csv"
    dfs.append(read_temp(url, name))

# Combine into one dataframe
data = pd.concat(dfs, ignore_index=True)
data.to_csv("global-temp.csv", index=False)

