path = #Path to data frame with the APSIM data for Beverly, MA
df = pd.read_csv(path)
rain_data = []
for y in np.arange(2000, 2022):
  curr = df.loc[df['year'] == y, ['rain']]
  rain_data.append(list(curr['rain']))
rain_data = np.array(rain_data)
daily_means = np.mean(rain_data, axis = 0)
lower_end = {}
for y in np.arange(2022, 2056):
  increase = daily_means * (1 + (0.00142 * (y - 2022 + 1)))
  lower_end[y] = increase
todflower = pd.DataFrame(lower_end)
upper_end = {}
for y in np.arange(2022, 2056):
  increase = daily_means * (1 + (0.00287 * (y - 2022 + 1)))
  upper_end[y] = increase
todfupper = pd.DataFrame(upper_end)
