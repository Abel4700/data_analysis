# Read the historical data file
import pandas as pd
df = pd.read_excel('C:/Users/al.hagos/Desktop/MIC/Fish/Thesis/hist.xlsx')
# Display the DataFrame
print(df.head())
# Convert all columns to numeric data types
df = df.apply(pd.to_numeric, errors='coerce')

# Check for missing values
if df.isnull().values.any():
    print("DataFrame contains missing values. Please handle them before proceeding.")
else:
    # Your modeling code here
    # Train HOLT models and generate forecasts
    def train_holt_model(df, variable):
        # Example code for training HOLT model, replace with actual implementation
        pass

    # Train ARIMA models and generate forecasts
    def train_arima_model(df, variable):
        # Example code for training ARIMA model, replace with actual implementation
        pass

    # Plotting code for historical data and forecasts
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 8))
    for variable in df.columns[1:]:
        plt.plot(df['Year'], df[variable], label=f'{variable} (Historical)')

    plt.title('Historical Data')
    plt.xlabel('Year')
    plt.ylabel('Mean')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
