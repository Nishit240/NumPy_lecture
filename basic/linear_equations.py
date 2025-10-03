# 2x+y=5
# x−y=1
# AX=B
# A = [[2, 1], [-1, 1]]
# B = [5, 1]

import numpy as np

A = np.array([[2, 1],
              [1, -1]])

B = np.array([5, 1])

X = np.linalg.solve(A, B)
print(X)

print(f"The solution for the system of equations is: x = {X[0]}, y = {X[1]}")


# 3x+y=9
# x+2y=8
A = np.array([[3, 1],[1, 2]])
B = np.array([9, 8])
X = np.linalg.solve(A,B)
print(X)
print(f"The solution for the second system of equations is: x = {X[0]}, y = {X[1]}")

A = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
B = np.array([6, -4, 27])
X = np.linalg.solve(A,B)
print(f"x = {X[0]}, y = {X[1]}, z = {X[2]}")

A = np.array([[2, -1, 1], [-3, 2, -4], [1, 1, 1]])
B = np.array([8, -2 ,3])
x = np.linalg.solve(A,B)
print(f"x = {x[0]}, y = {x[1]}, z = {x[2]}")
