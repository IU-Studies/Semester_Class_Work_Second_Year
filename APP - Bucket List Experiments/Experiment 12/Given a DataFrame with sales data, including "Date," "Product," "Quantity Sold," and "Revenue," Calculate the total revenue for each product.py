# Given a DataFrame with sales data, including "Date," "Product," "Quantity Sold," and "Revenue," Calculate the total revenue for each product.

import pandas as pd

# Example DataFrame
data = {
    'Date': ['2024-11-01', '2024-11-02', '2024-11-01', '2024-11-02'],
    'Product': ['A', 'B', 'A', 'B'],
    'Quantity Sold': [10, 20, 15, 25],
    'Revenue': [100, 200, 150, 250]
}
df = pd.DataFrame(data)

# Calculate total revenue for each product
total_revenue_per_product = df.groupby('Product')['Revenue'].sum()

# Convert result to a DataFrame if needed
total_revenue_per_product_df = total_revenue_per_product.reset_index()

# Display result
print(total_revenue_per_product_df)
