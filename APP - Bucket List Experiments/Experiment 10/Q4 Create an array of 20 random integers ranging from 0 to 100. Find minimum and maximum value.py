# Create an array of 20 random integers ranging from 0 to 100. Find minimum and maximum value.

import numpy as np

random_array = np.random.randint(0, 101, 20)
minimum_value = np.min(random_array)
maximum_value = np.max(random_array)

print(minimum_value)
print(maximum_value)
