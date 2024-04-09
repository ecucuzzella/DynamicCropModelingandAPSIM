import pandas as pd
import numpy as np
path = #Path to data frame with the APSIM data for all counties
df = pd.read_csv(path)
grain_wt = df['Maize.Grain.Wt']
grain_wt = grain_wt / 0.000247105
acres = df['Acres']
grain_total_weight = grain_wt * acres
grams_per_bushel = 453*56
solution = grain_total_weight / grams_per_bushel
