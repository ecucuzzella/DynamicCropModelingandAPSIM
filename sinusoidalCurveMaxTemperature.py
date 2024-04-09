import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
path = #Path to data frame of Beverly met data
df = pd.read_csv(path)
df['DayID'] = np.arange(len(df))
def generating_sin_pred(theta = math.pi/400, b = 3, m = 10, alpha = 0.2):
  X = (np.arange(8030) * np.cos(theta)) - (m * np.sin(alpha * np.arange(8030)) * 
  np.sin(theta))
  Y = (np.arange(8030) * np.sin(theta)) + (m * np.sin(alpha * np.arange(8030)) * 
  np.cos(theta)) + b
  return X, Y
def generating_sin_accuracy(maxt, theta = math.pi/400, b = 3, m = 10, alpha = 0.2):
  X, Y = generating_sin_pred(theta, b, m, alpha)
  return np.sqrt(np.sum((np.array(maxt) - Y)**2))
def generate_a_random_grid(n_combos):
  theta = np.random.rand(n_combos) * math.pi/400
  b = np.random.rand(n_combos) * 30
  m = np.random.rand(n_combos) * 50
  alpha = np.random.rand(n_combos)
  combos = []
  for i in range(n_combos):
    curr = [theta[i], b[i], m[i], alpha[i]]
    combos.append(curr)
  return combos
combos = generate_a_random_grid(10000)
results = {}
for combo in combos:
  ex_var = generating_sin_accuracy(df['maxt'], theta = combo[0], b = combo[1], m = combo[2], alpha = combo[3])
  results[str(combo)] = ex_var
sorted_results = dict(sorted(results.items(), key=lambda item: item[1]))
keys = list(sorted_results.keys())
print(keys[0] + " ==> " + str(sorted_results[keys[0]]))
