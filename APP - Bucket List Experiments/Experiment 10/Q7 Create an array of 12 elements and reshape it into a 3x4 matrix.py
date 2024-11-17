#  Create an array of 12 elements and reshape it into a 3x4 matrix.

import numpy as np

array = np.arange(1, 13)
reshaped_matrix = array.reshape(3, 4)

print(reshaped_matrix)
