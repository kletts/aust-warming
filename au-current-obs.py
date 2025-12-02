
# CDS data request 
# this downloads the gridded monthly average temperature 
# data on a bounding box covering Australia  [-9, 112, -44, 160]

import cdsapi
import datetime
import netCDF4
import numpy as np 
import pandas as pd
import sys
import os
from dotenv import load_dotenv
load_dotenv()


ct = datetime.date.today() + datetime.timedelta(days=-30)

dataset = "reanalysis-era5-land-monthly-means"

request = {
    "product_type": ["monthly_averaged_reanalysis"],
    "variable": ["2m_temperature"],
    "year": [ ct.year ],
    "month": [ ct.month ],
    "time": ["00:00"],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [-9, 112, -44, 160]
}
target = 'download.nc'

client = cdsapi.Client(
    url="https://cds.climate.copernicus.eu/api", 
    key=os.getenv('CDSAPIKEY'))

client.retrieve(dataset, request, target)

# read netcdf ... etc
# data.dimensions: ('valid_time', 'latitude', 'longitude')

obs = netCDF4.Dataset('download.nc', 'r')
data = obs.variables['t2m']
long = obs.variables['longitude'][:]
lat = obs.variables['latitude'][:]

grid = pd.read_csv("au-anomaly-norm.csv") 
grid = grid[(grid['Month'] == ct.month)]

x = np.array(range(grid.shape[0]), dtype=float)

for i in range(grid.shape[0]): 
    j = np.abs(long - grid['long'].iloc[i]).argmin()
    k = np.abs(lat - grid['lat'].iloc[i]).argmin() 
    x[i] = data[0,k,j].data - 273.15 

grid['Date'] = ct
grid['ObsTemp'] =  x
grid.to_csv("au-current-obs.csv", index=False)