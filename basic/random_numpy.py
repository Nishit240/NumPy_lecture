
#Random Numbers in NumPy
import numpy as np
import random 

print('Random numbers between 0 and 10:', np.random.randint(1,10))
print('5 random numbers between 1 and 9 :', np.random.randint(1,10, 5))
print('3x4 array of random numbers :\n', np.random.randint(1,10,(3,4)))

print(np.random.rand())   # Single float between 0 and 1
print(np.random.rand(5))  # Array of 5 floats between 0 and 1
print(np.random.rand(3,2)) # 3x2 array of floats between 0 and 1

arr3 = np.array([10, 20, 30, 40, 50])
print(np.random.choice(arr3))  # Randomly choose 1 element from the array
print(np.random.choice(arr3,3))  # Randomly choose 3 element from the array

print(np.random.randint(1, 20,(3,3)))
print(np.random.rand(6))
arr4 = np.array([5, 10, 15, 20, 25, 30])
print(np.random.choice(arr4, 4))
