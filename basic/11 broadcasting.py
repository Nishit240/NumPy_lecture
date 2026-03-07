'''
single array broadcasting
'''

import numpy as np

arr = np.array([1, 2, 3])
# print("Original array:", arr)
broadcasted_arr = arr + 10
print("Broadcasted array:", broadcasted_arr)

'''
2D array broadcasting
'''

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([10, 20, 30])
# print("Original matrix:\n", matrix)
# print("Vector to broadcast:", vector)
broadcasted_matrix = matrix + vector
print("Broadcasted matrix:\n", broadcasted_matrix)

'''
error case: incompatible shapes
'''

matrix = np.array([[1, 2], [3, 4], [5, 6]])
vector = np.array([10, 20, 30])
# print("Original matrix:\n", matrix)
# print("Vector to broadcast:", vector)
# This will raise a ValueError due to incompatible shapes
try:
    broadcasted_matrix = matrix + vector
    print("Broadcasted matrix:\n", broadcasted_matrix)
except ValueError as e:
    print("Error during broadcasting:", e)


