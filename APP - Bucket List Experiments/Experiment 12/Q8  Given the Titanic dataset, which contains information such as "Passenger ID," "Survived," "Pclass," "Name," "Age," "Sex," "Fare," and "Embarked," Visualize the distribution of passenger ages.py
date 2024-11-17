# Given the Titanic dataset, which contains information such as "Passenger ID," "Survived," "Pclass," "Name," "Age," "Sex," "Fare," and "Embarked," 
# Visualize the distribution of passenger ages.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Passenger ID': [1, 2, 3, 4, 5, 6],
    'Survived': [0, 1, 1, 0, 1, 0],
    'Pclass': [3, 1, 3, 1, 2, 3],
    'Name': ['John Doe', 'Jane Smith', 'Alan Brown', 'Clara White', 'Emily Black', 'Tom Green'],
    'Age': [22, 38, 26, 35, 27, 2],
    'Sex': ['male', 'female', 'male', 'female', 'female', 'male'],
    'Fare': [7.25, 71.28, 7.92, 53.1, 11.5, 8.05],
    'Embarked': ['S', 'C', 'S', 'S', 'S', 'C']
}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=10, kde=True, color='skyblue')
plt.title('Distribution of Passenger Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
