import numpy as np

# 1D array
arr = np.array((1, 2, 3, 4, 5, 6, 7, 8))
print(f"1D array: {arr}")

'''indexing [0] [2] [-2]'''
print(f'arr[0] = {arr[0]}')  # Accessing the first element
print(f'arr[2] = {arr[2]}')  # Accessing the third element
print(f'arr[-2] = {arr[-2]}')  # Accessing the 2nd element from the end

'''fancy indexing [list of indices]'''
print(f"arr[[0,2,4]] = {arr[[0,2,4]]}")  # Accessing multiple elements using a list of indices


'''slicing  [start:stop:step]'''
print(f"arr[1:5] = {arr[1:5]}")  # Slicing from index 1 to 4
print(f"arr[:4] = {arr[:4]}")   # Slicing from the beginning to index 3
print(f"arr[4:] = {arr[4:]}")   # Slicing from index 4 to the end
print(f"arr[::2] = {arr[::2]}")  # Slicing with a step of 2 (every other element)
print(f"arr[1::2] = {arr[1::2]}")  # Slicing with a step of 2 starting from index 1 (every other element starting from the second element)
print(f"arr[::-1] = {arr[::-1]}")  # Slicing with a step of -1 (reversing the array)


# 2D array
arr2 = np.array([[1, 2, 3], 
                 [4, 5, 6],
                 [7, 8, 9]])
print(f"\n2D array:\n{arr2}")

'''indexing [row, column]'''
print(f"arr2[0, 1] = {arr2[0, 1]}")  # Accessing the element in the first row and second column
print(f"arr2[1, 0] = {arr2[1, 0]}")  # Accessing the element in the second row and first column


'''slicing [row_start:row_stop, col_start:col_stop]'''
print(f"arr2[1, 1:3] = {arr2[1, 1:3]}")  # Slicing the second row from  
print(f"arr2[0:2, 1] = {arr2[0:2, 1]}")  # Slicing the second column from the first two rows
print(f"arr2[:, 0] = {arr2[:, 0]}")  # Slicing the first column from all rows


# 3D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], 
                 [[7, 8, 9], [10, 11, 12]],
                 [[13, 14, 15], [16, 17, 18]]])
print(f"\n3D array:\n{arr3}")

'''indexing [block, row, column]'''
print(f"arr3[0, 1, 2] = {arr3[0, 1, 2]}")  # Accessing the element in the first block, second row, and third column

print(f"arr3[1, 0, 1:3] = {arr3[1, 0, 1:3]}")  # Slicing the first row of the second block from the second to third column


'''slicing [block_start:block_stop, row_start:row_stop, col_start:col_stop]'''
print(f"arr3[:, 0, 0] = {arr3[:, 0, 0]}")  # Slicing the first column of the first row from all blocks

print(f"arr3[0, :, :] = {arr3[0, :, :]}")  # Slicing all rows and columns from the first block

print(f"arr3[:, 1, :] = {arr3[:, 1, :]}")  # Slicing all rows and columns from the second row of all blocks

print(f"arr3[:, :, 1] = {arr3[:, :, 1]}")  # Slicing the second column from all rows and blocks

print(f"arr3[1, :, 1] = {arr3[1, :, 1]}")  # Slicing the second column from all rows of the second block

print(f"arr3[1, 1, :] = {arr3[1, 1, :]}")  # Slicing all columns from the second row of the second block

print(f"arr3[1, 1, 1] = {arr3[1, 1, 1]}")  # Accessing the element in the second block, second row, and second column

print(f"arr3[0, 0, 0] = {arr3[0, 0, 0]}")  # Accessing the element in the first block, first row, and first column


'''Boolean indexing'''
print(f"arr[arr > 5] = {arr[arr > 5]}")  # Boolean indexing to get elements greater than 5

