# Train ARIMA models and generate forecasts
arima_forecasts = {}
for variable, params in arima_params.items():
    arima_model = ARIMA(df[variable], order=params['order'])
    arima_fit = arima_model.fit()
    arima_forecasts[variable] = arima_fit.forecast(steps=5)[0]  # Forecast for 5 years (2024-2028)
