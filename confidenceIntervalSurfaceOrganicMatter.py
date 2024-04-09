som_sum = []
for y in np.arange(2000, 2022):
  year_yields = df.loc[df['year'] == y, ['SurfaceOrganicMatter.Wt']]
  year_cover = df.loc[df['year'] == y, ['SurfaceOrganicMatter.Cover']]
  som_sum.append(year_yields.sum()[0] / year_cover.sum()[0])
n = len(som_sum)
m = np.mean(som_sum)
se = scipy.stats.sem(som_sum)
h = se * scipy.stats.t.ppf((1 + 0.95) / 2.0, n-1)
print(m+h)
print(m-h)
