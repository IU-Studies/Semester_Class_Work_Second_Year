#  You have a dataset with weather data containing columns "Date," "City," "Temperature," "Humidity," "Wind Speed," and "Rainfall."
# Identify any correlations between temperature, humidity, and rainfall.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
data = {
    'Date': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04'],
    'City': ['City A', 'City A', 'City B', 'City B'],
    'Temperature': [20, 22, 15, 17],
    'Humidity': [60, 65, 70, 72],
    'Wind Speed': [10, 12, 8, 9],
    'Rainfall': [0, 5, 1, 0]
}
df = pd.DataFrame(data)

# Select relevant columns for correlation
correlation_data = df[['Temperature', 'Humidity', 'Rainfall']]

# Compute correlation matrix
correlation_matrix = correlation_data.corr()

# Print correlation matrix
print(correlation_matrix)

# Visualize the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between Temperature, Humidity, and Rainfall')
plt.show()
