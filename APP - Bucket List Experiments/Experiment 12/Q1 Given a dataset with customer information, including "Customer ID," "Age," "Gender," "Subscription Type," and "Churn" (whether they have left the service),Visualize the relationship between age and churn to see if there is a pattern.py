# Given a dataset with customer information, including "Customer ID," "Age," "Gender," "Subscription Type,
# " and "Churn" (whether they have left the service),
# Visualize the relationship between age and churn to see if there is a pattern.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('customer_data.csv')

print(data.head())

sns.boxplot(x='Churn', y='Age', data=data)
plt.title('Age Distribution by Churn')
plt.xlabel('Churn')
plt.ylabel('Age')
plt.show()

sns.kdeplot(data=data, x='Age', hue='Churn', fill=True)
plt.title('Age Distribution by Churn')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()
