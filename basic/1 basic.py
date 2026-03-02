# NumPy is a powerful library in Python for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

# speed is faster than list and tuple 
# less memory than list and tuple
# easy mathematical operations on arrays
# used in data science, machine learning, and scientific computing.

import numpy as np


print(np.__version__)
arr = np.array((1, 2, 3, 4, 5, 6, 7, 8))
print(type(arr))
print(f"Slicing  : {arr[1:3]}")
print(arr[1:6:2])
print(arr[2] + arr[3])
print(arr[2] - arr[3])
print(arr[2] * arr[3])
print(arr[2] / arr[3])



a = np.array([0, 1, 2, 3])  # From list
b = np.arange(0, 10, 2)   # Range with step
c = np.linspace(0, 1, 5) # Evenly spaced numbers
d = np.zeros((2, 3))     # All zeros
e = np.ones((3, 3))       # All ones
f = np.eye(3)           # Identity matrix
g = np.full((3, 3), 24)     # Full of a specific value
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)





arr1 = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])
print(arr1)
print(f"Slicing Entire row  : {arr1[1:2]}")
print(f"Slicing Entire row  : {arr1[1]}")
print(f"Slicing specific Coloum : {arr1[:, 1]}")



a = np.array(42)
print(a.ndim)

b = np.array([1, 2, 3, 4, 5])
print(b.ndim)

c = np.array([[1, 2, 3], 
              [4, 5, 6]])
print(c.ndim)
print('2nd element on 1st row: ', c[0, 1])
print(c[1, 1:3])

d = np.array([[[1, 2, 3], [4, 5, 6]], 
              [[7, 8, 9], [10, 11, 12]]])
print(d[0, 1, 2])
print('ndim:', d.ndim)



arr2 = np.array([1, 2, 3, 4], ndmin=5)
print(arr2)
print('shape of array :', arr2.shape)



arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8], ndmin=5)
print(arr3)
print('size of array :', arr3.size)


arr4 = np.array([[1, 2.4, 3], 
                 [4, 5, 6.3]])
print('arr4:', arr4)
print('dtype before:', arr4.dtype)

int_arr = arr4.astype(int)
print('astype:\n', int_arr)  
print('dtype after:', int_arr.dtype)

