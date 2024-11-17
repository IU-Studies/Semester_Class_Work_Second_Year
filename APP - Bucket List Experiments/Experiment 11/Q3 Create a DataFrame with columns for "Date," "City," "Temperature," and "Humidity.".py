# Create a DataFrame with columns for "Date," "City," "Temperature," and "Humidity." 
# Then Find the average temperature for each city. Identify the days when the temperature was above 30°C.

import pandas as pd

data = {
    "Date": ["2024-11-01", "2024-11-02", "2024-11-03", "2024-11-04", "2024-11-05"],
    "City": ["City A", "City B", "City A", "City B", "City A"],
    "Temperature": [32, 28, 35, 30, 29],
    "Humidity": [60, 65, 55, 70, 75]
}

df = pd.DataFrame(data)

average_temperature = df.groupby("City")["Temperature"].mean()

hot_days = df[df["Temperature"] > 30]

print("Average Temperature for each city:")
print(average_temperature)

print("\nDays when the temperature was above 30°C:")
print(hot_days)
