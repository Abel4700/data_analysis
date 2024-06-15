# Train HOLT models and generate forecasts
holt_forecasts = {}
for variable, params in holt_params.items():
    holt_model = ExponentialSmoothing(df[variable], trend='add', seasonal=None)
    holt_fit = holt_model.fit(smoothing_level=params['alpha'], smoothing_trend=params['gamma'])
    holt_forecasts[variable] = holt_fit.forecast(5)  # Forecast for 5 years (2024-2028)
