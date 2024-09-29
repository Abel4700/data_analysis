import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing

# Historical data
historical_data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Mental Health Counseling': [6, 8, 8, 8, 12, 13, 17],
    'Educational Support': [31, 29, 30, 32, 44, 39, 40],
    'Livelihood Support for Families': [9, 6, 7, 6, 15, 17, 20]
}

df = pd.DataFrame(historical_data)

# Function to train Exponential Smoothing (Holt) model and generate forecast for a specific variable
def train_holt_model(df, variable, alpha, gamma):
    holt_model = ExponentialSmoothing(df[variable], trend='add', seasonal=None, initialization_method="estimated")
    holt_fit = holt_model.fit(smoothing_level=alpha, smoothing_slope=gamma)
    forecast_values = holt_fit.forecast(steps=5)
    return forecast_values

# Plot historical data and forecasts for each variable separately
plt.figure(figsize=(12, 8))
for variable, alpha, gamma in [('Mental Health Counseling', 0.00, 0.00),
                               ('Educational Support', 0.20, 0.00),
                               ('Livelihood Support for Families', 0.00, 0.00)]:
    years = range(2024, 2029)  # Adjust the range to include 5 years for forecasts
    plt.plot(df['Year'], df[variable], label=f'{variable} (Historical)')
    forecast = train_holt_model(df, variable, alpha, gamma)
    plt.plot(years, forecast, label=f'{variable} (HOLT Forecast)')

plt.title('Forecasted Trends for Different Variables (Holt Model)')
plt.xlabel('Year')
plt.ylabel('Mean')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
