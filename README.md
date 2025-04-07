ARIMA Forecasting

This project uses an ARIMA (AutoRegressive Integrated Moving Average) model to forecast stock prices based on yearly historical data (1990–2009), accounting for events like a 1996 market crash and a 2002 boom.

The model parameters (p, d, q) are automatically selected using the auto_arima() function, which:
a. Tests for stationarity and applies differencing (d) if needed,
b. Evaluates multiple combinations of p and q (autoregression and moving average)
c. Selects the best model using the Akaike Information Criterion (AIC) for optimal accuracy and simplicity.

The trained model is then used to predict the stock price for the year 2010.
