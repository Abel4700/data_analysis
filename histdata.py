import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt

# Read the historical data file into DataFrame
file_path = 'C:/Users/al.hagos/Desktop/MIC/Fish/Thesis/historicaldata.csv'
df = pd.read_csv(file_path)

# Extract the total row and remove it from the DataFrame
total_row = df[df['Year'] == 'Total']
df = df[df['Year'] != 'Total']

# Convert all columns to numeric data types except 'Year'
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Check for missing values and print the count of missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Check if there are any missing values
if df.isnull().values.any():
    print("DataFrame contains missing values. Handling missing values by filling with column mean.")
    df = df.fillna(df.mean())
else:
    print("DataFrame loaded successfully.")

# Display the cleaned DataFrame and the total row
print("Cleaned DataFrame:")
print(df)
print("Total Row:")
print(total_row)

# Function to train HOLT model and generate forecast
def train_holt_model(df, variable):
    holt_model = ExponentialSmoothing(df[variable], trend='add', seasonal=None)
    holt_fit = holt_model.fit()
    forecast_values = holt_fit.forecast(steps=4)
    return forecast_values

# List to store HOLT forecasts for each variable
holt_forecasts = {}

# Loop through each variable in the DataFrame (excluding 'Year')
for variable in df.columns[1:]:
    holt_forecasts[variable] = train_holt_model(df, variable)

# Display the HOLT forecasts
print("HOLT Forecasts:")
print(holt_forecasts)

# Plot historical data and forecasts for each variable
plt.figure(figsize=(12, 8))
for variable in df.columns[1:]:
    plt.plot(df['Year'], df[variable], label=f'{variable} (Historical)')
    plt.plot(range(2024, 2028), holt_forecasts[variable], label=f'{variable} (HOLT Forecast)')

plt.title('Forecasted Trends for Different Variables')
plt.xlabel('Year')
plt.ylabel('Mean')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
