
# New source: https://www.ncei.noaa.gov
# Reads global temperature data

read_temp <- function(url, region) { 
    readr::read_csv(url, skip=3, col_types="cn") |> 
    dplyr::renmae(AvTemp = Anomaly) |> 
    dplyr::mutate(Region = region, 
                  Date = as.Date(paste0(Date, "01"), "%Y%m%d")) }

area <- c("Globe"="globe", 
          "North"="nhem", 
          "South"="shem") 

yr <- format(Sys.Date() %m-% months(1), "%Y")
url <- glue::glue("https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/{area}/land_ocean/tavg/1/0/1850-{yr}/data.csv")    
url <- setNames(url, names(area))

data <- imap_dfr(url, read_temp) 

