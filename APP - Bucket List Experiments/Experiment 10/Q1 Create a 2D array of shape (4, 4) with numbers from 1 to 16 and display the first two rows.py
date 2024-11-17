#  Create a 2D array of shape (4, 4) with numbers from 1 to 16 and display the first two rows

import numpy as np

array = np.arange(1, 17).reshape(4, 4)
print(array[:2])
