import numpy as np

# creating an 1-D array
arr = np.arange(10)
print(arr)


# 2x3 array of all ones and a 3x2 array of all zeros
ones_array = np.ones((2, 3))
zeros_array = np.zeros((3, 2))

print("Ones Array:\n", ones_array)
print("Zeros Array:\n", zeros_array)


# 3x3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)


#2D array with values ranging from 1 to 12 with shape (3, 4)
array_2d = np.arange(1, 13).reshape((3, 4))
print(array_2d)
