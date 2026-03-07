'''
| Function       | Result                       | Notes                  |
| -------------- | ---------------------------- | ---------------------- |
| `vstack`       | vertical stack               | same number of columns |
| `hstack`       | horizontal stack             | same number of rows    |
| `stack`        | stack along new axis         | creates new dimension  |
| `dstack`       | stack along depth (3rd axis) | good for 3D arrays     |
| `column_stack` | stack 1D arrays as columns   | creates 2D array       |
'''

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])


print("Array a:", a)
print("Array b:", b)
vstacked = np.vstack((a, b))
stacked0= np.stack((a,b), axis=0)
print("Vertical stack:\n", vstacked)

hstacked = np.hstack((a,b))
stacked1= np.stack((a,b), axis=1)
print("Horizontal stack:\n", hstacked)

dstacked = np.dstack((a, b))
print("Depth stack:\n", dstacked)
print("Shape:", dstacked.shape)

col_stacked = np.column_stack((a, b))
print("Column stack:\n", col_stacked)
