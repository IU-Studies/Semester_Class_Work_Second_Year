# Create two 3x3 matrices and perform Matrix multiplication (both element-wise and dot product).

import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

element_wise_multiplication = matrix1 * matrix2
dot_product = np.dot(matrix1, matrix2)

print(element_wise_multiplication)
print(dot_product)
