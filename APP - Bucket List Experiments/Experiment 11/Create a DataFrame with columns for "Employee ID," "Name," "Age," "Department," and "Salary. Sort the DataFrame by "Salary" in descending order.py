# Create a DataFrame with columns for "Employee ID," "Name," "Age," "Department," and "Salary. Sort the DataFrame by "Salary" in descending order.

import pandas as pd

data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 28, 35, 40],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"],
    "Salary": [55000, 60000, 75000, 50000, 65000]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values(by="Salary", ascending=False)

print(sorted_df)
