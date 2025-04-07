import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

# Load CSV file (make sure it's in the same directory as this script)
filename = "stock_prices_with_crash_and_boom.csv"
if not os.path.exists(filename):
    raise FileNotFoundError(f"'{filename}' not found. Make sure it's in the same directory as this script.")

data = pd.read_csv(filename)

# Prepare data for modeling
X = data[['Year']]
y = data['Stock_Price (€)']

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)
pred_2010 = model.predict([[2010]])[0]

# Extend data for plotting
years = data['Year'].values
prices = data['Stock_Price (€)'].values
years_extended = np.append(years, 2010)
prices_extended = np.append(prices, pred_2010)

# Plot the stock price evolution
plt.figure(figsize=(10, 6))
plt.plot(years, prices, marker='o', label='Historical Price (Crash + Boom)')
plt.plot(2010, pred_2010, 'ro', label=f'Predicted 2010: €{pred_2010:.2f}')
plt.axvline(x=1996, color='gray', linestyle='--', alpha=0.6, label='1996 Crash')
plt.axvline(x=2002, color='green', linestyle='--', alpha=0.6, label='2002 Boom')
plt.title('Stock Price Evolution (1990–2010) with Market Events')
plt.xlabel('Year')
plt.ylabel('Stock Price (€)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Print predicted price
print(f"Predicted stock price for 2010: €{pred_2010:.2f}")
