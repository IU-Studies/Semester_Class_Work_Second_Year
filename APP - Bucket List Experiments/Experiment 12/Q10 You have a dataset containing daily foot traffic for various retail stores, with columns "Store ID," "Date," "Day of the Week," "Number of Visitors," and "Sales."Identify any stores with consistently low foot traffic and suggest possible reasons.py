# You have a dataset containing daily foot traffic for various retail stores, with columns "Store ID," "Date," "Day of the Week," 
# "Number of Visitors," and "Sales."
# Identify any stores with consistently low foot traffic and suggest possible reasons

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Store ID': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
    'Date': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-01', '2024-11-02', '2024-11-03',
             '2024-11-01', '2024-11-02', '2024-11-03', '2024-11-01', '2024-11-02', '2024-11-03'],
    'Day of the Week': ['Monday', 'Tuesday', 'Wednesday', 'Monday', 'Tuesday', 'Wednesday',
                        'Monday', 'Tuesday', 'Wednesday', 'Monday', 'Tuesday', 'Wednesday'],
    'Number of Visitors': [50, 45, 55, 20, 18, 22, 35, 30, 40, 15, 10, 12],
    'Sales': [500, 450, 550, 200, 180, 220, 350, 300, 400, 150, 100, 120]
}
df = pd.DataFrame(data)

avg_foot_traffic = df.groupby('Store ID')['Number of Visitors'].mean().reset_index()
avg_foot_traffic.columns = ['Store ID', 'Avg Visitors']

threshold = avg_foot_traffic['Avg Visitors'].quantile(0.10)
low_traffic_stores = avg_foot_traffic[avg_foot_traffic['Avg Visitors'] <= threshold]

print("Stores with low foot traffic:")
print(low_traffic_stores)

plt.figure(figsize=(10, 6))
sns.barplot(data=avg_foot_traffic, x='Store ID', y='Avg Visitors', palette='viridis')
plt.axhline(y=threshold, color='red', linestyle='--', label='Low Traffic Threshold')
plt.title('Average Foot Traffic by Store')
plt.xlabel('Store ID')
plt.ylabel('Average Number of Visitors')
plt.legend()
plt.tight_layout()
plt.show()
