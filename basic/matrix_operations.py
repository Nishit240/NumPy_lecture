import numpy as np

#2. Dimensions of a Matrix print(A.ndim)
A = np.array([[1, 2],[3,4]])
B = np.array([[5,6],[7,8]])

#1. Transpose of a Matrix  Flip rows into columns.
print(A.T)

print(A + B)
print(A - B)
print(A * B)

#3. Dot product of two matrices.
print('Dot product :\n',np.dot(A, B))

#4. Inverse of a Matrix.
print(np.linalg.inv(A))
print(np.linalg.det(A))

#6. Check if Matrix is singular.  If det(A) = 0, then matrix is singular.  Otherwise, it is non-singular.  The determinant is calculated as np.linalg.det(A)

if np.linalg.det(A)!=0:
    print('Inverse of A:\n', np.linalg.inv(A))
else:
    print('The matrix is singular and hence, it does not have an inverse.')


restaurant_types = np.array(['biryani', 'chinese', 'pizza', 'burger', 'cafe'])
vectorized_upper = np.vectorize(str.upper)
print("Vectorized Upper", vectorized_upper(restaurant_types))
