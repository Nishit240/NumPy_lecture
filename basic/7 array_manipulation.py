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


'''
.ravel() -> View
.flatten() -> Copy
.reshape() -> View (if possible) or Copy (if necessary)
'''

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D array:\n", arr_2d)
print("Raveled array (view):\n", arr_2d.ravel())
print("Flattened array (copy):\n", arr_2d.flatten())


print("flattened array :\n",reshaped_arr.flatten())
arr2 =np.arange(1,21).reshape(4,5).flatten()
print("flattened array from 4x5 :\n",arr2)