# Given a DataFrame with some missing values in various columns, Identify columns with missing values

import pandas as pd

data = {
    "Employee ID": [101, 102, 103, None, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", None],
    "Age": [25, None, 28, 35, 40],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"],
    "Salary": [55000, 60000, None, 50000, 65000]
}

df = pd.DataFrame(data)

columns_with_missing = df.columns[df.isnull().any()]

print(columns_with_missing)
