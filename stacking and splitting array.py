import numpy as np

#stacking

# 1.Vertical Stacking
#Create two 2x3 arrays and stack them vertically to form a 4x3 array.

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
vertically_stacked = np.vstack((arr1, arr2))
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)
print("Vertically stacked array:\n", vertically_stacked)


# 2.Horizontal Stacking
#Create two 3x2 arrays and stack them horizontally to form a 3x4 array
arr1 = np.array([[1, 2], [3, 4], [5, 6]])
arr2 = np.array([[7, 8], [9, 10], [11, 12]])
horizontally_stacked = np.hstack((arr1, arr2))
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)
print("Horizontally stacked array:\n", horizontally_stacked)


# 3.Depth Stacking (3D stacking)
#Create two 3x3 arrays and stack them along a new third axis (depth) to form a 3x3x2 array
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
depth_stacked = np.dstack((arr1, arr2))
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)
print("Depth stacked array:\n", depth_stacked)


# 4.column stacking
#Create two 1D arrays of 4 elements each. Stack them as columns into a 4x2 array
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
column_stacked = np.column_stack((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Column-stacked array:\n", column_stacked)


# 5.Row-wise Stacking
# Create two 1D arrays of 5 elements each. Stack them as rows into a 2x5 array.
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
row_stacked = np.row_stack((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Row-stacked array:\n", row_stacked)


#splitting 

# 1.Splitting into Equal Parts
#Create a 1D array of 20 elements. Split it into 4 equal parts.
arr = np.arange(20)
split_arr = np.split(arr, 4)
print("Original array:", arr)
print("Split arrays:", split_arr)


# 2.Vertical Split
#Create a 6x4 array with values from 0 to 23. Split this array into two equal parts vertically
arr = np.arange(24).reshape(6, 4)
vertical_split = np.vsplit(arr, 2)
print("Original array:\n", arr)
print("Vertically split arrays:")
for part in vertical_split:
    print(part)


# 3.Horizontal Split
#Create a 4x6 array with values from 0 to 23. Split this array into three equal parts horizontally.
arr = np.arange(24).reshape(4, 6)
horizontal_split = np.hsplit(arr, 3)
print("Original array:\n", arr)
print("Horizontally split arrays:")
for part in horizontal_split:
    print(part)


# 4.Depth Split
# Create a 3x3x6 array with values from 0 to 53. Split this array into three equal parts along the depth axis.
arr = np.arange(54).reshape(3, 3, 6)
depth_split = np.dsplit(arr, 3)
print("Original 3D array:\n", arr)
print("Depth split arrays:")
for part in depth_split:
    print(part)

# 5.Advanced Stacking
#Create three 2x2 arrays. Stack them along a new axis to form a 2x2x3 array.
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.array([[9, 10], [11, 12]])
stacked = np.stack((arr1, arr2, arr3), axis=-1)
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)
print("Array 3:\n", arr3)
print("Stacked array along a new axis:\n", stacked)

