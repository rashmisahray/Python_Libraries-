import numpy as np

# adding  elements
# Create a 1D array with values from 0 to 4. Add the elements 5 and 6 to the end of this array.
arr = np.array([0, 1, 2, 3, 4])
arr_extended = np.append(arr, [5, 6])
print("Original array:", arr)
print("Array after adding elements:", arr_extended)


# Inserting Elements into a 1D Array
# Create a 1D array with values from 0 to 4. Insert the element 10 at the second position.
arr = np.array([0, 1, 2, 3, 4])
arr_with_insert = np.insert(arr, 1, 10)
print("Original array:", arr)
print("Array after insertion:", arr_with_insert)


# Appending Rows to a 2D Array
# Create a 2x3 array with values from 1 to 6. Append a new row [7, 8, 9] to this array
arr = np.array([[1, 2, 3], [4, 5, 6]])
new_row = np.array([[7, 8, 9]])
arr_with_row = np.append(arr, new_row, axis=0)
print("Original array:\n", arr)
print("Array after appending a new row:\n", arr_with_row)


# Appending Columns to a 2D Array
# Create a 2x2 array with values from 1 to 4. Append a new column [5, 6] to this array.
arr = np.array([[1, 2], [3, 4]])
new_col = np.array([[5], [6]])
arr_with_col = np.append(arr, new_col, axis=1)
print("Original array:\n", arr)
print("Array after appending a new column:\n", arr_with_col)


# Deleting Elements from a 1D Array
# Create a 1D array with values from 0 to 9. Remove the element at index 4
arr = np.arange(10)
arr_removed = np.delete(arr, 4)
print("Original array:", arr)
print("Array after removing the element at index 4:", arr_removed)


#Deleting Rows from a 2D Array
#Create a 3x3 array with values from 1 to 9. Remove the second row.
arr = np.arange(1, 10).reshape(3, 3)
arr_removed_row = np.delete(arr, 1, axis=0)
print("Original array:\n", arr)
print("Array after removing the second row:\n", arr_removed_row)


# Deleting Columns from a 2D Array
# Create a 4x4 array with values from 0 to 15. Remove the third column.
arr = np.arange(16).reshape(4, 4)
arr_removed_col = np.delete(arr, 2, axis=1)
print("Original array:\n", arr)
print("Array after removing the third column:\n", arr_removed_col)


#Removing Multiple Elements
# Create a 1D array with values from 0 to 9. Remove the elements at indices 1, 3, and 5
arr = np.arange(10)
arr_removed_multiple = np.delete(arr, [1, 3, 5])
print("Original array:", arr)
print("Array after removing elements at indices 1, 3, and 5:", arr_removed_multiple)


#Concatenating Multiple Arrays
# Create three 1D arrays: a = [1, 2], b = [3, 4], and c = [5, 6]. Concatenate them into a single 1D array.
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
concatenated = np.concatenate((a, b, c))
print("Arrays a, b, c:", a, b, c)
print("Concatenated array:", concatenated)


#Concatenating Along a New Axis
# Create two 1D arrays: x = [10, 20] and y = [30, 40]. Stack them along a new axis to form a 2x2 array
x = np.array([10, 20])
y = np.array([30, 40])
stacked_new_axis = np.stack((x, y), axis=0)
print("Array x:", x)
print("Array y:", y)
print("Stacked along a new axis:\n", stacked_new_axis)




