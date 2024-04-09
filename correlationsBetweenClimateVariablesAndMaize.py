import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path_met = #Path to dataframe with randomized data
path_sim = #Path to dataframe with simulation results
met = pd.read_csv(path_met)
sim = pd.read_excel(path_sim)
maxt, mint, radn, rain, swe, vp = []
for year in np.arange(2023, 2031):
  subset = met.loc[met['year'] == year, :]
  maxt.append(np.mean(list(subset['maxt'])))
  mint.append(np.mean(list(subset['mint'])))
  rain.append(np.mean(list(subset['rain'])))
  radn.append(np.mean(list(subset['radn'])))
  vp.append(np.mean(list(subset['vp'])))
  swe.append(np.mean(list(subset['swe'])))
df = pd.DataFrame({'year': np.arange(2023, 2031), 'maize.aboveground.wt': list(sim['Maize.AboveGround.Wt']), 'maxt': maxt, 'mint': mint, 'radn': radn, 'rain': rain, 'vp': vp, 'swe': swe})
correlation_matrix = df.loc[df['year'] > 2023, list(df.columns.values)[1:]].corr()
df_shifted = pd.DataFrame({'maize.aboveground.wt': list(df['maize.aboveground.wt'])[1:], 'maxt': df['maxt'][:-1], 'mint': df['mint'][:-1], 'radn': df['radn'][:-1], 'rain': df['rain'][:-1], 'vp': df['vp'][:-1], 'swe': df['swe'][:-1]})
correlation_matrix_shifted = df_shifted.corr()
z = np.polyfit(list(df_shifted['rain']), list(df_shifted['maize.aboveground.wt']), 1)
z
