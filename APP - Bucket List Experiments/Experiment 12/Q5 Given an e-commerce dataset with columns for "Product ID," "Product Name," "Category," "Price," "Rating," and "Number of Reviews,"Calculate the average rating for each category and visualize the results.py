# Given an e-commerce dataset with columns for "Product ID," "Product Name," "Category," "Price," "Rating," 
# and "Number of Reviews,"Calculate the average rating for each category and visualize the results.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Product ID': [101, 102, 103, 104, 105, 106],
    'Product Name': ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F'],
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home', 'Home'],
    'Price': [200, 150, 50, 40, 100, 80],
    'Rating': [4.5, 4.0, 3.5, 4.2, 4.8, 4.6],
    'Number of Reviews': [100, 50, 200, 150, 80, 90]
}
df = pd.DataFrame(data)

avg_rating_per_category = df.groupby('Category')['Rating'].mean().reset_index()

print(avg_rating_per_category)

plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Rating', data=avg_rating_per_category, palette='viridis')
plt.title('Average Rating by Category')
plt.xlabel('Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
