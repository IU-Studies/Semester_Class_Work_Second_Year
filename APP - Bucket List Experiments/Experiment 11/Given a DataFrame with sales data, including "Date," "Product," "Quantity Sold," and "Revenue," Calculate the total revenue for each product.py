# Given a DataFrame with sales data, including "Date," "Product," "Quantity Sold," and "Revenue," Calculate the total revenue for each product.

import pandas as pd

data = {
    "Date": ["2024-11-01", "2024-11-02", "2024-11-03", "2024-11-04", "2024-11-05"],
    "Product": ["A", "B", "A", "C", "B"],
    "Quantity Sold": [10, 5, 8, 3, 7],
    "Revenue": [100, 50, 80, 30, 70]
}

df = pd.DataFrame(data)

total_revenue = df.groupby("Product")["Revenue"].sum()

print(total_revenue)
