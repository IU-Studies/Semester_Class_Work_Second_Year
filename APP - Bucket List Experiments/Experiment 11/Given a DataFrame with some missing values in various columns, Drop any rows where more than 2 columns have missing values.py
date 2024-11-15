# Given a DataFrame with some missing values in various columns, Drop any rows where more than 2 columns have missing values

import pandas as pd

data = {
    "A": [1, None, 3, None, 5],
    "B": [None, 2, None, 4, None],
    "C": [None, None, 6, 7, 8],
    "D": [9, 10, 11, 12, 13]
}

df = pd.DataFrame(data)

filtered_df = df.dropna(thresh=len(df.columns)-2)

print(filtered_df)
