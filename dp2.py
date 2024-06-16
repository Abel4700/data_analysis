import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Historical data
historical_data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Individual Case Management': [69, 77, 81, 102, 129, 141, 148],
    'Family Reunification Support': [60, 61, 57, 71, 87, 97, 101],
    'Psychosocial Support': [67, 71, 76, 95, 119, 125, 131],
    'Alternative Care Arrangement': [50, 56, 58, 74, 92, 104, 109],
    'Community-Based Child Protection': [64, 71, 75, 95, 124, 132, 137],
    'Shelter Provision': [11, 8, 10, 6, 10, 6, 9],
    'WASH': [11, 9, 9, 11, 8, 9, 12],
    'Health and Nutrition': [13, 10, 10, 10, 19, 17, 16]
}

df = pd.DataFrame(historical_data)

# Function to train ARIMA model and generate forecast for a specific variable
def train_arima_model(df, variable, order):
    arima_model = ARIMA(df[variable], order=order)
    arima_fit = arima_model.fit()
    forecast_values = arima_fit.forecast(steps=5)
    return forecast_values

# Plot historical data and forecasts for each variable separately
plt.figure(figsize=(12, 8))
for variable, order in [('Individual Case Management', (0, 1, 0)),
                        ('Family Reunification Support', (0, 1, 0)),
                        ('Psychosocial Support', (0, 1, 0)),
                        ('Alternative Care Arrangement', (0, 1, 0)),
                        ('Community-Based Child Protection', (0, 1, 0)),
                        ('Shelter Provision', (0, 0, 0)),
                        ('WASH', (0, 0, 0)),
                        ('Health and Nutrition', (0, 0, 0))]:
    years = range(2024, 2029)  # Adjust the range to include 5 years for forecasts
    plt.plot(df['Year'], df[variable], label=f'{variable} (Historical)')
    forecast = train_arima_model(df, variable, order)
    plt.plot(years, forecast, label=f'{variable} (ARIMA Forecast)')

plt.title('Forecasted Trends for Different Variables (ARIMA Model)')
plt.xlabel('Year')
plt.ylabel('Mean')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
