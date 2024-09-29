# Import pandas and HOLT model
import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing

# Read the historical data file into DataFrame
df = pd.read_csv('C:/Users/al.hagos/Desktop/MIC/Fish/Thesis/historicaldata.csv')

# Function to train HOLT model and generate forecast
def train_holt_model(df, variable):
    # Your code to train HOLT model using df
    # Example:
    holt_model = ExponentialSmoothing(df[variable], trend='add')
    holt_fit = holt_model.fit()
    forecast_values = holt_fit.forecast(steps=5)
    return forecast_values

# List to store HOLT forecasts for each variable
holt_forecasts = {}

# Loop through each variable in the DataFrame
for variable in df.columns[1:]:
    holt_forecasts[variable] = train_holt_model(df, variable)

# Display the HOLT forecasts
print(holt_forecasts)
