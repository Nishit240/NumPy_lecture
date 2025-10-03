import numpy as np

arr = np.arange(1, 13)
print("Original array",arr)

# Reshape the array to 3x4
reshaped_arr = arr.reshape(3, 4)
print("Reshaped array to 3x4 :\n",reshaped_arr)

reshaped_arr2 = arr.reshape(4,3)
print("Reshaped array to 4x3 :\n",reshaped_arr2)

reshaped_auto =arr.reshape(2,-1)
print("2,-1\n",reshaped_auto)
reshape_auto =arr.reshape(-1,2)
print("-1, 2\n",reshaped_auto)
print(reshaped_arr)
print("flattened array :\n",reshaped_arr.flatten())

arr2 =np.arange(1,21).reshape(4,5).flatten()

# | Function       | Result                       | Notes                  |
# | -------------- | ---------------------------- | ---------------------- |
# | `vstack`       | vertical stack               | same number of columns |
# | `hstack`       | horizontal stack             | same number of rows    |
# | `stack`        | stack along new axis         | creates new dimension  |
# | `dstack`       | stack along depth (3rd axis) | good for 3D arrays     |
# | `column_stack` | stack 1D arrays as columns   | creates 2D array       |


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

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
