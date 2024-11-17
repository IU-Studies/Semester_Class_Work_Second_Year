# You have a dataset with weather data containing columns "Date," "City," "Temperature," "Humidity," "Wind Speed," and "Rainfall."
# Plot temperature trends over time for multiple cities.

import pandas as pd
import matplotlib.pyplot as plt

# Example dataset
data = {
    'Date': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-01', '2024-11-02', '2024-11-03'],
    'City': ['City A', 'City A', 'City A', 'City B', 'City B', 'City B'],
    'Temperature': [20, 22, 21, 15, 17, 16],
    'Humidity': [60, 65, 63, 70, 72, 68],
    'Wind Speed': [10, 12, 11, 8, 9, 10],
    'Rainfall': [0, 5, 2, 1, 0, 3]
}
df = pd.DataFrame(data)

# Convert 'Date' to datetime for better handling
df['Date'] = pd.to_datetime(df['Date'])

# Plot temperature trends
plt.figure(figsize=(10, 6))
for city in df['City'].unique():
    city_data = df[df['City'] == city]
    plt.plot(city_data['Date'], city_data['Temperature'], marker='o', label=city)

plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend(title='City')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
