import pandas as pd
import numpy as np
path = #Path to dataframe with historical Beverly meteorological data 
df = pd.read_csv(path)
counts = [0,0,0,0,0,0,0,0,0,0,0,0]
for y in range(2000, 2022):
  subset = df.loc[df['year'] == y, :]
  i = 0
  m = 0
  while i < len(subset):
    rain_sub = list(subset['rain'])[i:i+31]
    i = i + 31
    m += 1
    rain_sub = [1 if x > 0 else 0 for x in rain_sub]
    counts[m - 1] += rain_sub.count(1)
counts = [c/(30 * (2022-2000)) for c in counts]
