# Create a DataFrame with a "Date" column and a "Sales" column containing daily sales data:
# Resample the data to calculate the total sales for each month.

import pandas as pd

data = {
    "Date": ["2024-11-01", "2024-11-02", "2024-11-03", "2024-11-04", "2024-11-05"],
    "Sales": [100, 150, 200, 250, 300]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.resample("M", on="Date")["Sales"].sum()

print(monthly_sales)
