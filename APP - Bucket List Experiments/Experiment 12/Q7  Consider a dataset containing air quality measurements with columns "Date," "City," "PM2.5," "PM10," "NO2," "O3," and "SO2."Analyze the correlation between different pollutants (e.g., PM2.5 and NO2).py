#  Consider a dataset containing air quality measurements with columns "Date," "City," "PM2.5," "PM10," "NO2," "O3," and "SO2."
# Analyze the correlation between different pollutants (e.g., PM2.5 and NO2).

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
data = {
    'Date': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04', '2024-11-05'],
    'City': ['City A', 'City A', 'City A', 'City A', 'City A'],
    'PM2.5': [35, 50, 45, 80, 30],
    'PM10': [60, 75, 70, 90, 55],
    'NO2': [20, 25, 22, 40, 18],
    'O3': [30, 28, 35, 25, 20],
    'SO2': [15, 18, 16, 25, 12]
}
df = pd.DataFrame(data)

# Select only pollutant columns
pollutants = df[['PM2.5', 'PM10', 'NO2', 'O3', 'SO2']]

# Compute the correlation matrix
correlation_matrix = pollutants.corr()

# Print the correlation matrix
print(correlation_matrix)

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Between Pollutants')
plt.show()
