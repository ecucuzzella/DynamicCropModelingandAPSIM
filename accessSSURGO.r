library(apsimx)
library(soilDB)
soil_bev <- get_ssurgo_soil_profile(lonlat = c(-71, 43))
write(soil_bev, "soil_data_beverly.txt")
