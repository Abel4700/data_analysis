from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

# Function to train ARIMA model and generate forecast
def train_arima_model(df, variable):
    # Your code to train ARIMA model and generate forecast
    # This part will depend on the specific implementation of ARIMA for your data
    return forecast_values

# List to store ARIMA forecasts for each variable
arima_forecasts = {}

# Loop through each variable in the DataFrame
for variable in df.columns[1:]:
    arima_forecasts[variable] = train_arima_model(df, variable)

# Display the ARIMA forecasts
print(arima_forecasts)
# Train ARIMA models and generate forecasts
arima_forecasts = {}
for variable, params in arima_params.items():
    arima_model = ARIMA(df[variable], order=params['order'])
    arima_fit = arima_model.fit()
    arima_forecasts[variable] = arima_fit.forecast(steps=5)[0]  # Forecast for 5 years (2024-2028)
