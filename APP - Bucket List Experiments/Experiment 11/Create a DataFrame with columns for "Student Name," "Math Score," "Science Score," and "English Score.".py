# Create a DataFrame with columns for "Student Name," "Math Score," "Science Score," and "English Score." 
# Calculate the average score for each student. Identify students who scored below 50 in any subject.

import pandas as pd

data = {
    "Student Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math Score": [85, 42, 78, 56, 91],
    "Science Score": [90, 55, 88, 60, 76],
    "English Score": [88, 48, 80, 54, 89]
}

df = pd.DataFrame(data)
df["Average Score"] = df[["Math Score", "Science Score", "English Score"]].mean(axis=1)

below_50 = df[(df["Math Score"] < 50) | (df["Science Score"] < 50) | (df["English Score"] < 50)]

print("Average Scores:")
print(df)
print("\nStudents who scored below 50 in any subject:")
print(below_50)
