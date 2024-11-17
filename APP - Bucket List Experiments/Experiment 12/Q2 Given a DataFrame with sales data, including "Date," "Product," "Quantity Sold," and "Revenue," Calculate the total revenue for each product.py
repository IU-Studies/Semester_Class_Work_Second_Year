# Given a DataFrame with sales data, including "Date," "Product," "Quantity Sold," and "Revenue," Calculate the total revenue for each product.

import pandas as pd

data = {
    'Date': ['2024-11-01', '2024-11-02', '2024-11-01', '2024-11-02'],
    'Product': ['A', 'B', 'A', 'B'],
    'Quantity Sold': [10, 20, 15, 25],
    'Revenue': [100, 200, 150, 250]
}
df = pd.DataFrame(data)

total_revenue_per_product = df.groupby('Product')['Revenue'].sum()

total_revenue_per_product_df = total_revenue_per_product.reset_index()

print(total_revenue_per_product_df)
