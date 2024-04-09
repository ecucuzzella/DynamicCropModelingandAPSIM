import pandas as pd
import numpy as np
import random
from sklearn.metrics import explained_variance_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
path = #Path to data frame with the Beverly met data
df = pd.read_csv(path)
df['month'] = [int(val[5:7]) for val in df['Date']]
for_training = np.random.randint(0, len(df), int(len(df)*0.9))
all = np.arange(len(df))
for_testing = np.array([number for number in all if number not in for_training])
train_x = df.loc[for_training, ['maxt', 'mint', 'radn', 'month']]
train_y = df.loc[for_training, ['vp']]
test_x = df.loc[for_testing, ['maxt', 'mint', 'radn', 'month']]
test_y = df.loc[for_testing, ['vp']]
poly_x = PolynomialFeatures(degree = 3).fit(train_x)
poly_x_train = poly_x.transform(train_x)
poly_x_test = poly_x.transform(test_x)
lr = LinearRegression()
lr.fit(poly_x_train, train_y)
pred_train = lr.predict(poly_x_train)
pred_test = lr.predict(poly_x_test)
curr_forecast_df = #Path to the forecasted daily temperature data
forecast_data = curr_forecast_df.loc[:, ['maxt', 'mint', 'year', 'month']]
poly_forecast = poly_x.transform(forecast_data)
predictions = lr.predict(poly_forecast)
