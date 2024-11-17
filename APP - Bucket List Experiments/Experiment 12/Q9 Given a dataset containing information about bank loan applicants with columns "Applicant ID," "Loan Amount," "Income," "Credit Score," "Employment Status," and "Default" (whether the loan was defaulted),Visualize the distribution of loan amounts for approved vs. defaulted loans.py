#  Given a dataset containing information about bank loan applicants with columns "Applicant ID," "Loan Amount," "Income," "Credit Score," "Employment Status," and "Default" (whether the loan was defaulted),
# Visualize the distribution of loan amounts for approved vs. defaulted loans.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
data = {
    'Applicant ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Loan Amount': [5000, 10000, 15000, 20000, 12000, 7000, 30000, 25000],
    'Income': [30000, 40000, 50000, 60000, 45000, 35000, 80000, 75000],
    'Credit Score': [700, 650, 620, 710, 680, 640, 720, 680],
    'Employment Status': ['Employed', 'Employed', 'Self-Employed', 'Employed', 'Employed', 'Self-Employed', 'Employed', 'Employed'],
    'Default': [0, 0, 1, 0, 1, 0, 0, 1]
}
df = pd.DataFrame(data)

# Visualize the distribution of loan amounts for approved vs. defaulted loans
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Loan Amount', hue='Default', kde=True, bins=10, palette='coolwarm', multiple='stack')
plt.title('Distribution of Loan Amounts by Default Status')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.legend(title='Default', labels=['Approved', 'Defaulted'])
plt.grid(True)
plt.tight_layout()
plt.show()
