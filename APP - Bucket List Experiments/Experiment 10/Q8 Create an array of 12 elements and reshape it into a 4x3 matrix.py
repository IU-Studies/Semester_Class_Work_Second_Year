# Create an array of 12 elements and reshape it into a 4x3 matrix

import numpy as np

array = np.arange(1, 13)
reshaped_matrix = array.reshape(4, 3)

print(reshaped_matrix)
