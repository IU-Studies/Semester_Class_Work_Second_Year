# Given a DataFrame containing stock prices with columns "Date," "Open," "Close," "High," and "Low". Plot the closing prices over time

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": ["2024-11-01", "2024-11-02", "2024-11-03", "2024-11-04", "2024-11-05"],
    "Open": [100, 105, 110, 108, 112],
    "Close": [102, 107, 112, 109, 115],
    "High": [103, 108, 113, 110, 116],
    "Low": [99, 104, 109, 106, 111]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

plt.plot(df["Date"], df["Close"], marker='o', linestyle='-', color='b')
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Stock Closing Prices Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
