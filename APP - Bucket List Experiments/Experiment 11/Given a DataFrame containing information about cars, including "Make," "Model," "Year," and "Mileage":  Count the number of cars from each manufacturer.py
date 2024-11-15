# Given a DataFrame containing information about cars, including "Make," "Model," "Year," and "Mileage":
# Count the number of cars from each manufacturer.

import pandas as pd

data = {
    "Make": ["Toyota", "Honda", "Ford", "Toyota", "Honda", "Ford"],
    "Model": ["Corolla", "Civic", "Focus", "Camry", "Accord", "Fusion"],
    "Year": [2020, 2021, 2020, 2019, 2022, 2019],
    "Mileage": [15000, 12000, 18000, 25000, 10000, 22000]
}

df = pd.DataFrame(data)

car_count = df["Make"].value_counts()

print(car_count)
