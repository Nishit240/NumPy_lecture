import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
sorted_data = np.sort(data)

print(f"Mean: {np.mean(sorted_data)}")
print(f"Median: {np.median(sorted_data)}")
print(f"Standard Deviation: {np.std(sorted_data)}")
print(f"Variance: {np.var(sorted_data)}")
print(f"Sum: {np.sum(sorted_data)}")
print(f"Minimum: {np.min(sorted_data)}")
print(f"Maximum: {np.max(sorted_data)}")
print(f"Range: {np.max(sorted_data) - np.min(sorted_data)}")
print(f"Median: {sorted_data[len(sorted_data)//2]}")
print(f"Mode: {np.bincount(data).argmax()}")

arr = np.array([ 1, 1, 1, 2, 2, 2, 2, 3, 3])
unique_vals = np.unique(arr)
counts = np.unique(arr, return_counts=True)

print("Unique values:", unique_vals)
print("Counts:", counts)


data = np.array([3, 7, 1, 9, 4])
percentile_50 = np.percentile(data, 50)  # median
percentile_25 = np.percentile(data, 25)
percentile_75 = np.percentile(data, 75)
print("25th percentile:", percentile_25)
print("50th percentile (median):", percentile_50)
print("75th percentile:", percentile_75)

# Cumulative Sum and Product
cumsum = np.cumsum(data)
cumprod = np.cumprod(data)
print("Cumulative sum:", cumsum)
print("Cumulative product:", cumprod)

min_index = np.argmin(data)
max_index = np.argmax(data)
print("Index of min:", min_index)
print("Index of max:", max_index)



matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("Mean of columns:", np.mean(matrix, axis=0))
print("Mean of rows:", np.mean(matrix, axis=1))
print("Max of columns:", np.max(matrix, axis=0))  # along columns
print("Max of rows:", np.max(matrix, axis=1))     # along rows

scores = np.array([[85, 92, 78],
                   [79, 85, 88],
                   [90, 91, 95],
                   [70, 75, 80],
                   [88, 84, 82]])

# Find the index of the overall max value
max_index = np.unravel_index(np.argmax(scores), scores.shape)

print("Index of maximum score (row, column):", max_index)
print("Maximum score:", scores[max_index])
