import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
# Historical data
historical_data_2 = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Alternative Care Arrangement': [50, 56, 58, 74, 92, 104, 109],
    'Community-Based Child Protection': [64, 71, 75, 95, 124, 132, 137],
    'Shelter Provision': [11, 8, 10, 6, 10, 6, 9]
}

df_2 = pd.DataFrame(historical_data_2)
# Function to train ARIMA model and generate forecast for a specific variable
def train_arima_model(df, variable, order):
    arima_model = ARIMA(df[variable], order=order)
    arima_fit = arima_model.fit()
    forecast_values = arima_fit.forecast(steps=5)
    return forecast_values

# Plot historical data and forecasts for each variable separately
plt.figure(figsize=(12, 8))
for variable, order in [('Alternative Care Arrangement', (1, 1, 0)),
                        ('Community-Based Child Protection', (1, 1, 0)),
                        ('Shelter Provision', (1, 1, 0))]:
    years = range(2024, 2029)  # Adjust the range to include 5 years for forecasts
    plt.plot(df_2['Year'], df_2[variable], label=f'{variable} (Historical)')
    forecast = train_arima_model(df_2, variable, order)
    plt.plot(years, forecast, label=f'{variable} (ARIMA Forecast)')

plt.title('Forecasted Trends for Different Variables (ARIMA Model) - Group 2')
plt.xlabel('Year')
plt.ylabel('Mean')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
