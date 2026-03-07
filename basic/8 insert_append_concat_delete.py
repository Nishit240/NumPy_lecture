'''
np.insert(array, index, values, axis=None)
axis = 0 , row wise
axis = 1 , column wise 
'''

import numpy as np

arr = np.array([1,2,3])
new_arr = np.insert(arr, 1, 10, axis=0)
print("Original array:", arr)
print("New array after insertion:", new_arr)


'''
insert in 2D array
'''

arr_2d = np.array([[1, 2], [5, 6]])
new_arr_2d = np.insert(arr_2d, 1, [3,4], axis=0)
print("Original 2D array:\n", arr_2d)
print("New 2D array after insertion:\n", new_arr_2d)


'''
append a row to the end of the 2D array
'''

arr = np.array([1,2,3])
new_arr = np.append(arr, [4, 5, 6])
print("Original array:", arr)
print("New array after appending:", new_arr)


'''
concatenate two arrays

'''

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

concatenated_arr = np.concatenate((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Concatenated array:", concatenated_arr)

arr1 = np.arange(1,6)
arr2 = np.arange(6,11)
arr3 = np.arange(11,17)
combine = np.concatenate((arr1, arr2, arr3))
print(combine)
print("Compatibility Shaper ", arr1.shape == arr2.shape)
print("Compatibility Shaper ", arr1.shape == arr3.shape)



'''
delete an element from an array
'''

arr = np.array([1, 2, 3, 4, 5])
new_arr = np.delete(arr, 2)
print("Original array:", arr)
print("New array after deletion:", new_arr)

'''
delete in 2D array
'''
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
new_arr_2d = np.delete(arr_2d, 1, axis=0)
print("Original 2D array:\n", arr_2d)
print("New 2D array after deletion:\n", new_arr_2d)