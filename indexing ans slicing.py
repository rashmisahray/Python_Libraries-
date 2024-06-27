# 4x4 NumPy array with values ranging from 1 to 16. Extract a 2x2 subarray from the top-right corner
import numpy as np

arr = np.arange(1, 17).reshape(4, 4)
subarray = arr[:2, 2:]
print("Original array:\n", arr)
print("Subarray:\n", subarray)

# Create a 3x3 NumPy array with values from 10 to 18. Access the element at the second row and third column
arr = np.arange(10, 19).reshape(3, 3)
element = arr[1, 2]
print("Array:\n", arr)
print("Element at second row, third column:", element)

#Create a 5x5 array of all ones. Modify the elements in the middle 3x3 subarray to be 7
arr = np.ones((5, 5))
arr[1:4, 1:4] = 7
print("Modified array:\n", arr)

#  Create a 1D NumPy array of the first 10 natural numbers and reverse the array.
arr = np.arange(1, 11)
reversed_arr = arr[::-1]
print("Original array:", arr)
print("Reversed array:", reversed_arr)

#  Create a 1D array of numbers from 0 to 9. Select only the elements that are greater than 5
arr = np.arange(10)
greater_than_5 = arr[arr > 5]
print("Original array:", arr)
print("Elements greater than 5:", greater_than_5)

#Create a 3x3 array with values ranging from 1 to 9. Extract the diagonal elements
arr = np.arange(1, 10).reshape(3, 3)
diagonal = np.diag(arr)
print("Original array:\n", arr)
print("Diagonal elements:", diagonal)


