# Australian Monthly Temperature Anomaly 

Calculates the monthly temperature anomaly for Australia on a 1 degree grid basis. 

Anomaly is calculated as the difference between: 

- 'Normal Tempertaures' from Bureau of Meterology [long term temperature record](http://www.bom.gov.au/climate/data/acorn-sat/), with interpolation from observation station data to the 1 degree grid 

- 'Observed Temperatures' from Copurnicus [Climate Data Store](https://cds.climate.copernicus.eu), the `reanalysis-era5-land-monthly-means` measured as 2m surface temperatures, downloaded at 0.5 degree grid with the observation nearest to the 1 degree grid used. 

The app is published to [Observable Data Apps](https://klettsch.observablehq.cloud/australia-monthly-warming/)

