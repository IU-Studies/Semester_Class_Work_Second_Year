#Create two 3x3 matrices and perform Matrix addition on and subtraction.

import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

addition_result = matrix1 + matrix2
subtraction_result = matrix1 - matrix2

print(addition_result)
print(subtraction_result)
