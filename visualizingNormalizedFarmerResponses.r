library(ggplot2)
library(maps)
library(mapdata)

new_england <- ggplot2::map_data('state', region = c('Massachusetts', 'New Hampshire'))

df <- data.frame(longitude = c(-71.07, -71.14, -71.23, -71.30, -71.14, -70.95, -70.93, -71.08, -70.88, -71.05, -71.57), latitude = c(41.95, 42.16, 42.44, 42.42, 42.45, 42.47, 42.58, 42.58, 42.56, 42.94, 43.33), precip = c(0,.125,1,.625,.666,.2,.55,.5,.142,.667,0), unpredictable = c(0,.875,.142,.75,.778,.2,.778,1,1,1,.8))

ggplot() +
  geom_polygon(data = new_england, aes(x = long, y = lat, group = group), fill = "#a8e4a0", color = "black") +
  geom_point(data = df, aes(x = longitude, y = latitude, color = unpredictable)) +
  scale_color_gradient(low = "green", high = "darkgreen") +
  labs(title = "Farmer Opinions on Impact of Unpredictable Weather on Yield", x = "Longitude", y = "Latitude", color = "Rating")
