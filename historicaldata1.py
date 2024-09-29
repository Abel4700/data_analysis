import pandas as pd
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing, ARIMA
import matplotlib.pyplot as plt

# Define historical data
data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Individual Case Management': [69, 77, 81, 102, 129, 141, 148],
    'Family Reunification Support': [60, 61, 57, 71, 87, 97, 101],
    'Mental Health Counseling': [6, 8, 8, 8, 12, 13, 17],
    'Psychosocial Support': [67, 71, 76, 95, 119, 125, 131],
    'Alternative Care Arrangement': [50, 56, 58, 74, 92, 104, 109],
    'Educational Support': [31, 29, 30, 32, 44, 39, 40],
    'Community Based CP': [64, 71, 75, 95, 124, 132, 137],
    'Shelter Provision': [11, 8, 10, 6, 10, 6, 9],
    'Livelihood Support for Families': [9, 6, 7, 6, 15, 17, 20],
    'WASH': [11, 9, 9, 11, 8, 9, 12],
    'Health and Nutrition': [13, 10, 10, 10, 19, 17, 16]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Define HOLT and ARIMA parameters
holt_params = {
    'Mental Health Counseling': {'alpha': 0.0, 'gamma': 0.0},
    'Educational Support': {'alpha': 0.20, 'gamma': 0.0},
    'Livelihood Support for Families': {'alpha': 0.0, 'gamma': 0.0}
}

arima_params_group2 = {
    'Individual Case Management': {'order': (0, 1, 0)},
    'Family Reunification Support': {'order': (0, 1, 0)},
    'Psychosocial Support': {'order': (0, 1, 0)},
    'Alternative Care Arrangement': {'order': (0, 1, 0)},
    'Community Based CP': {'order': (0, 1, 0)}
}

arima_params_group3 = {
    'Shelter Provision': {'order': (0, 0, 0)},
    'WASH': {'order': (0, 0, 0)},
    'Health and Nutrition': {'order': (0, 0, 0)}
}

# Function to train HOLT model and generate forecast
def train_holt_model(df, variable, params):
    model = ExponentialSmoothing(df[variable], trend='add', seasonal=None)
    model_fit = model.fit(smoothing_level=params['alpha'], smoothing_slope=params['gamma'])
    forecast = model_fit.forecast(steps=5)
    return forecast

# Function to train ARIMA model and generate forecast
def train_arima_model(df, variable, params):
    model = ARIMA(df[variable], order=params['order'])
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=5)
    return forecast

# Plot historical data and forecasts for each variable separately in groups
def plot_group(df, group_params, model_type, title):
    plt.figure(figsize=(14, 10))
    for variable, params in group_params.items():
        years = range(2024, 2029)
        plt.plot(df['Year'], df[variable], label=f'{variable} (Historical)')
        if model_type == 'HOLT':
            forecast = train_holt_model(df, variable, params)
        else:
            forecast = train_arima_model(df, variable, params)
        plt.plot(years, forecast, label=f'{variable} ({model_type} Forecast)')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Mean')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot each group separately
plot_group(df, holt_params, 'HOLT', 'Forecasted Trends for HOLT Model Variables')
plot_group(df, arima_params_group2, 'ARIMA', 'Forecasted Trends for ARIMA Model Variables (Differencing)')
plot_group(df, arima_params_group3, 'ARIMA', 'Forecasted Trends for ARIMA Model Variables (No Differencing)')
