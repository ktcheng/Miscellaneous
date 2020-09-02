  
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:30:45 2020
@author: Kellen Cheng
"""

# Relevant Facts
healthy_mask = 0.7
sick_mask = 0.05
both_mask = 0.015

# Relevant Import Statements
from sklearn import linear_model
from sklearn.metrics import max_error
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter
from florida_regression import quad_regression
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

### Data Retrieval
link = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
link2 = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"
data = pd.read_csv(link)

### Data Pruning
states = data["state"]
invalid_rows = [i for i in range(states.size) if states[i] != "Florida"]
data = data.drop(data.index[invalid_rows])
data = data.drop("fips", axis = 1)

contracted_dates = data["date"]
date_format = [datetime.strptime(item, "%Y-%m-%d") for item in contracted_dates]

### Data Analysis

# Visualization of Total Cases
fig, ax = plt.subplots(figsize = (25, 7))

plot_variable = "cases"
date_display_format = DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(date_display_format)
ax.xaxis.set_major_locator(mdates.DayLocator(interval = 5))
ax.scatter(date_format, data[plot_variable])

plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("Total Cases/Date in Florida")
plt.grid()

# Visualization of New Cases
fig, ax = plt.subplots(figsize = (25, 7))
data["total cases"] = data["cases"]
data["cases"] = data["cases"].diff()

plot_variable = "cases"
date_display_format = DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(date_display_format)
ax.xaxis.set_major_locator(mdates.DayLocator(interval = 5))
ax.scatter(date_format, data[plot_variable])

plt.xlabel("Date")
plt.ylabel("New Cases")
plt.title("New Cases/Date in Florida")
plt.grid()

# Visualization of New Cases Trend
fig, ax = plt.subplots(figsize = (25, 7))

plot_variable = "cases"
date_display_format = DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(date_display_format)
ax.xaxis.set_major_locator(mdates.DayLocator(interval = 5))

X_param = [i for i in range(38, 113)] # N.B. Change this to match # of days
test = data[plot_variable].tolist()[38:]
ax.scatter(date_format[38:], test)
ax.scatter(date_format[38:], quad_regression(X_param, test))

plt.xlabel("Date")
plt.ylabel("New Cases Trends")
plt.title("Trend of New Cases/Date in Florida")
plt.grid()

# Visualization of New Deaths
fig, ax = plt.subplots(figsize = (25, 7))

plot_variable = "deaths"
date_display_format = DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(date_display_format)
ax.xaxis.set_major_locator(mdates.DayLocator(interval = 5))
ax.scatter(date_format, data[plot_variable])

plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.title("Total Deaths/Date in Florida")
plt.grid()

# Visualization of Rolling Average Cases
fig, ax = plt.subplots(figsize = (25, 7))
time_period = 7
data["moving cases"] = data["cases"].rolling(window = time_period).mean()

plot_variable = "moving cases"
date_display_format = DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(date_display_format)
ax.xaxis.set_major_locator(mdates.DayLocator(interval = 5))

test = data[plot_variable].tolist()[38:]
quad_result = quad_regression(X_param, test)
ax.scatter(date_format, data[plot_variable])
ax.scatter(date_format[38:], quad_result)

plt.xlabel("Date")
plt.ylabel("New Cases")
plt.title("New Cases/Date in Florida")
plt.grid()

# Visualization of Rolling Average Deaths
time_period = 7
data["deaths"] = data["deaths"].diff()
data["moving deaths"] = data["deaths"].rolling(window = time_period).mean()

fig, ax = plt.subplots(figsize = (25, 7))
plot_variable = "moving deaths"
date_display_format = DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(date_display_format)
ax.xaxis.set_major_locator(mdates.DayLocator(interval = 5))
ax.scatter(date_format, data[plot_variable])

plt.xlabel("Date")
plt.ylabel("New Deaths")
plt.title("New Deaths/Date in Florida")
plt.grid()

### Linear Regression Prediction

# Data Retrieval and Pruning
X = contracted_dates
Y = data["total cases"].tolist()[1:] # Already moving from above
Z = data["cases"].tolist()[1:]
starting_date = 30 # April 1 is 30 days from March 1
days_list = [[i] for i in range(1, len(X))]

X = days_list
X = X[starting_date:]
Y = Y[starting_date:]
Z = Z[starting_date:]

regression_model = linear_model.LinearRegression()
regression_model.fit(X, Y)
# print(regression_model.score(X, Y)) # Outputs 0.9866

# Data Prediction
total_cases_est = regression_model.predict(X)
error = max_error(Y, total_cases_est)

future_period = 120 # We want to predict 1 month in advance
X_trend = [[i] for i in range(starting_date, starting_date + future_period)]
Y_trend_est = regression_model.predict(X_trend)

Y_trend_max = [Y_trend_est[i] + error for i in range(len(Y_trend_est))]
Y_trend_min = [Y_trend_est[i] - error for i in range(len(Y_trend_est))]

# Plotting
date_zero = datetime.strptime(data["date"].tolist()[starting_date], "%Y-%m-%d")
prev_dates = []
x_ticks = []

step_size = 5
curr_date = date_zero
x_current = starting_date
n = int(future_period / step_size)

for i in range(0, n):
    prev_dates.append(str(curr_date.day) + "/" + str(curr_date.month))
    x_ticks.append(x_current)
    curr_date = curr_date + timedelta(days = step_size)
    x_current = x_current + step_size
    pass
pass

fig, ax = plt.subplots(figsize = (30, 7))
X = [i for i in range(38, 120)] # N.B. Change this to match # of days
plt.scatter(X, Y)

plt.plot(X_trend, Y_trend_est, color='green', linewidth=2)
plt.plot(X_trend, Y_trend_max, color='red', linewidth=1, linestyle='dashed')
plt.plot(X_trend, Y_trend_min, color='red', linewidth=1, linestyle='dashed')

plt.xlim(starting_date, starting_date + future_period)
plt.xticks(x_ticks, prev_dates)

plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("Total Cases Estimate (1 Month)")
plt.grid()
