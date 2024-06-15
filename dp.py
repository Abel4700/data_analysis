import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Historical data
historical_data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Individual Case Management': [69, 77, 81, 102, 129, 141, 148],
    'Family Reunification Support': [60, 61, 57, 71, 87, 97, 101],
    'Psychosocial Support': [67, 71, 76, 95, 119, 125, 131],
    'Alternative Care Arrangement': [50, 56, 58, 74, 92, 104, 109],
    'Community Based CP': [64, 71, 75, 95, 124, 132, 137],
    'Shelter Provision': [11, 8, 10, 6, 10, 6, 9],
    'WASH': [11, 9, 9, 11, 8, 9, 12],
    'Health and Nutrition': [13, 10, 10, 10, 19, 17, 16],
    'Mental Health Counseling': [6, 8, 8, 8, 12, 13, 17],
    'Educational Support': [31, 29, 30, 32, 44, 39, 40],
    'Livelihood Support for Families': [9, 6, 7, 6, 15, 17, 20]
}

df = pd.DataFrame(historical_data)

# Function to train ARIMA model and generate forecast for a specific variable
def train_arima_model(df, variable, order):
    arima_model = ARIMA(df[variable], order=order)
    arima_fit = arima_model.fit()
    forecast_values = arima_fit.forecast(steps=5)
    return forecast_values

# Function to train Holt model and generate forecast for a specific variable
def train_holt_model(df, variable):
    holt_model = ExponentialSmoothing(df[variable], trend='add', seasonal=None)
    holt_fit = holt_model.fit()
    forecast_values = holt_fit.forecast(steps=5)
    return forecast_values

# Plotting grouped variables with forecasts
def plot_group(group, title, forecast_function, order=None):
    plt.figure(figsize=(12, 8))
    years_forecast = range(2024, 2029)
    
    for variable in group:
        plt.plot(df['Year'], df[variable], label=f'{variable} (Historical)', marker='o')
        if forecast_function == 'arima':
            forecast = train_arima_model(df, variable, order)
        elif forecast_function == 'holt':
            forecast = train_holt_model(df, variable)
        plt.plot(years_forecast, forecast, label=f'{variable} (Forecast)', marker='x')

    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Mean')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Group 1: Individual Case Management, Family Reunification Support, Psychosocial Support
group1 = ['Individual Case Management', 'Family Reunification Support', 'Psychosocial Support']
plot_group(group1, 'Forecasted Trends for Group 1 Variables (ARIMA Model)', 'arima', (0, 1, 0))

# Group 2: Alternative Care Arrangement, Community Based CP, Shelter Provision
group2 = ['Alternative Care Arrangement', 'Community Based CP', 'Shelter Provision']
plot_group(group2, 'Forecasted Trends for Group 2 Variables (ARIMA Model)', 'arima', (0, 1, 0))

# Group 3: WASH, Health and Nutrition, Mental Health Counseling, Educational Support, Livelihood Support for Families
group3_arima = ['WASH', 'Health and Nutrition']
group3_holt = ['Mental Health Counseling', 'Educational Support', 'Livelihood Support for Families']

plot_group(group3_arima, 'Forecasted Trends for Group 3 Variables (ARIMA Model)', 'arima', (0, 1, 0))
plot_group(group3_holt, 'Forecasted Trends for Group 3 Variables (Holt Model)', 'holt')
