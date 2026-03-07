'''
np.split()
equal

np.hsplit()
split along columns

np.vsplit()
split along rows
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6 ,7, 8, 9])

print("Original array:", arr)
# Split into 3 equal parts
split_arr = np.split(arr, 3)
print("Split into 3 equal parts:", split_arr)

# Split into 4 parts (last part will have the remaining elements)
'''
split_arr = np.split(arr, 4)
print("Split into 4 parts:", split_arr) # ValueError
'''


# Split along columns
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array:\n", arr_2d)
h_split = np.hsplit(arr_2d, 3)
print("Split along columns:\n", h_split)

# Split along rows
v_split = np.vsplit(arr_2d, 3)
print("Split along rows:\n", v_split)