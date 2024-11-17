# You have a dataset containing air quality measurements with columns "Date," "City," "PM2.5," "PM10," "NO2," "O3," and "SO2."
# Identify trends or spikes in pollution over time for a specific city

import pandas as pd
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

# Convert 'Date' to datetime for better handling
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for a specific city (e.g., 'City A')
city_data = df[df['City'] == 'City A']

# Plot pollutants over time
plt.figure(figsize=(12, 8))

for pollutant in ['PM2.5', 'PM10', 'NO2', 'O3', 'SO2']:
    plt.plot(city_data['Date'], city_data[pollutant], marker='o', label=pollutant)

plt.title('Pollution Trends Over Time for City A')
plt.xlabel('Date')
plt.ylabel('Pollutant Level (µg/m³)')
plt.legend(title='Pollutants')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
