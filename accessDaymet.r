library(apsimx)
library(daymetr)
library(reshape2)
library(dplyr)
met_data_beverly <- get_daymet2_apsim_met(lonlat = c(-70.88, 42.56), years = c(2000:2021))
met_data_beverly <- impute_apsim_met(met_data_beverly, method = "mean")
beverly_full <- data.frame(year = met_data_beverly$year, day = met_data_beverly$day, maxt = met_data_beverly$maxt, mint = met_data_beverly$mint, rain = met_data_beverly$rain, radn = met_data_beverly$radn, vp = met_data_beverly$vp, swe = met_data_beverly$swe)
head(berkshire_full)
beverly_full$Date <- as.Date(paste(beverly_full$year, beverly_full$day, sep="/"), format="%Y/%j")
head(beverly_full)
write.csv(beverly_full, "Desktop/met_data_beverly.csv", row.names = FALSE)
header = "noname.met 
site =  noname 
latitude = 42.56 
longitude = -70.88 
tav = 10.6868767123288 
amp = 10.717095890411"
write(header, "Desktop/met_data_beverly.txt")
