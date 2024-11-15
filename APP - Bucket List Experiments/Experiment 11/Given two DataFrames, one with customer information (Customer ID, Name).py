# Given two DataFrames, one with customer information (Customer ID, Name) and another with order details (Customer ID, Product, Price), 
# perform the following:
# Merge the two DataFrames on "Customer ID."

import pandas as pd

customers = {
    "Customer ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
}

orders = {
    "Customer ID": [1, 2, 1],
    "Product": ["Laptop", "Phone", "Tablet"],
    "Price": [1000, 500, 300]
}

df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

merged_df = pd.merge(df_customers, df_orders, on="Customer ID")

print(merged_df)
