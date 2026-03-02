import numpy as np 

arr = np.array([10, 20, 30, 40 ,50])

print("Sum of all elements in the array : ", np.sum(arr))

print("Mean of all elements in the array : ", np.mean(arr))

print("Median of all elements in the array : ", np.median(arr))

print("Standard Deviation of all elements in the array : ", round(np.std(arr), 3))

print("Variance of all elements in the array : ", np.var(arr))

print("Minimum value in the array : ", np.min(arr))

print("Maximum value in the array : ", np.max(arr))

print("Index of minimum value in the array : ", np.argmin(arr)) 

print("Index of maximum value in the array : ", np.argmax(arr))


# opperation

arr2 = np.array([1, 2, 3])
print("Cumulative sum of the array : ", np.cumsum(arr2))

print("Cumulative product of the array : ", np.cumprod(arr2))

print("Array after adding 10 to each element : ", arr2 + 10)

print("Array after multiplying each element by 2 : ", arr2 * 2)

print("Array after raising each element to the power of 3 : ", arr2 ** 3)

print("Array after applying square root to each element : ", np.sqrt(arr2))