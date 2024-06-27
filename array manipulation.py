import numpy as np

# Reshape and Flatten
#Create a 3x4 array with values from 0 to 11. Reshape it to a 2x6 array and then flatten it to a 1D array
arr = np.arange(12).reshape(3, 4)
reshaped = arr.reshape(2, 6)
flattened = reshaped.flatten()
print("Original array:\n", arr)
print("Reshaped array:\n", reshaped)
print("Flattened array:", flattened)


#Transposing an Array
#Create a 2x5 array with values from 1 to 10. Transpose the array.
arr = np.arange(1, 11).reshape(2, 5)
transposed = arr.T
print("Original array:\n", arr)
print("Transposed array:\n", transposed)

# Broadcasting Operations
# Create a 3x3 array of all twos and add a 1D array of three ones to each row
arr = np.full((3, 3), 2)
ones = np.array([1, 1, 1])
result = arr + ones
print("Original array:\n", arr)
print("1D array of ones:", ones)
print("Result after broadcasting:\n", result)

#Boolean Masking
#Create a 4x4 array with random integers between 0 and 9. Create a mask to select all elements that are even.
np.random.seed(1)  # For reproducibility
arr = np.random.randint(0, 10, size=(4, 4))
even_mask = arr % 2 == 0
even_elements = arr[even_mask]
print("Original array:\n", arr)
print("Even mask:\n", even_mask)
print("Even elements:", even_elements)

#Advanced Fancy Indexing
#Create a 3x3 array with values from 0 to 8. Use fancy indexing to reorder the array such that the first row becomes the second, the second row becomes the last, and the last row becomes the first.
arr = np.arange(9).reshape(3, 3)
reordered_arr = arr[[2, 0, 1], :]
print("Original array:\n", arr)
print("Reordered array:\n", reordered_arr)





