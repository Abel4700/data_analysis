# Plot historical data and forecasts for each variable
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))
for variable in df.columns[1:]:
    plt.plot(df['Year'], df[variable], label=f'{variable} (Historical)')
    plt.plot(range(2024, 2028), holt_forecasts[variable], label=f'{variable} (HOLT Forecast)')
    plt.plot(range(2024, 2028), arima_forecasts[variable], label=f'{variable} (ARIMA Forecast)')

plt.title('Forecasted Trends for Different Variables')
plt.xlabel('Year')
plt.ylabel('Mean')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
