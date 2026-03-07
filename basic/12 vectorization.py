'''
operation apply on entire array without the need for explicit loops, making code more concise and efficient.
100x faster than loops
'''

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2
print("Result of addition:", result)
result = arr1 * arr2
print("Result of multiplication:", result)
result = arr1 * 2
print("Result of multiplication with scalar:", result)