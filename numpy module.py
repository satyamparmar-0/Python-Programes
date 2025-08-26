import numpy as np

# -------------------------------
# 1. Creating Basic Arrays
# -------------------------------

# Creating a 2x2 array filled with zeros (int type)
zero = np.zeros((2, 2), dtype=int)
print("Zero Array:\n", zero)

# Creating a 3x2 array filled with ones (float type)
one = np.ones((3, 2), dtype=float)
print("\nOne Array:\n", one)

# Creating arrays using arange
arr1 = np.arange(1, 9)
print("\nArray 1 (arange from 1 to 8):\n", arr1)

arr2 = np.arange(1, 10, 3)  # From 1 to 9 with step of 3
print("\nArray 2 (arange from 1 to 9 with step 3):\n", arr2)

# -------------------------------
# 2. Array Reshaping & Utilities
# -------------------------------

# Flatten the array (convert to 1D)
flattened = arr2.flatten()
print("\nFlattened arr2:\n", flattened)

# Reshape the array to 1x3
reshaped = arr2.reshape(1, 3)
print("\nReshaped arr2 to (1x3):\n", reshaped)

# Transpose of array (only changes if 2D or more)
transposed = reshaped.T
print("\nTransposed reshaped arr2:\n", transposed)

# Get unique elements
unique_elements = np.unique(arr2)
print("\nUnique elements in arr2:\n", unique_elements)

# Standard deviation of the array
std_dev = np.std(arr2)
print("\nStandard Deviation of arr2:\n", std_dev)

# Cumulative sum of the array
cumsum_arr2 = np.cumsum(arr2)
print("\nCumulative Sum of arr2:\n", cumsum_arr2)

# -------------------------------
# 3. Generating Random Arrays
# -------------------------------

# Random integers between 30 and 70 (size 5)
arr3 = np.random.randint(30, 70, size=5)
print("\n" + "*"*5 + " Random Integer Array: " + "#"*5)
print(arr3)

# -------------------------------
# 4. Array Properties & Operations
# -------------------------------

arr = np.array([[1, 2], [4, 5]])
arr1 = np.array([[6, 4], [3, 5]])

print("\nArray arr:\n", arr)
print("Array arr1:\n", arr1)

# Type and structure
print("\nType of arr:", type(arr))
print("Shape of arr:", arr.shape)
print("Dimensions of arr:", arr.ndim)

# Maximum elements
print("\nMaximum element in arr:", arr.max())
print("Maximum elements in each row of arr:", arr.max(axis=1))

# Sum operations
print("\nSum of all elements in arr:", arr.sum())
print("Element-wise addition (arr + arr1):\n", arr + arr1)
print("Element-wise multiplication (arr * arr1):\n", arr * arr1)
print("Matrix multiplication (arr.dot(arr1)):\n", arr.dot(arr1))

# -------------------------------
# 5. Mathematical Functions
# -------------------------------

# Square root of elements in arr1
sqrt_arr1 = np.sqrt(arr1)
print("\nSquare root of arr1:\n", sqrt_arr1)

# Using np.add function
sum_arrs = np.add(arr, arr1)
print("\nSum using np.add:\n", sum_arrs)

# -------------------------------
# 6. Statistical Functions
# -------------------------------

mean_val = np.mean(arr)
median_val = np.median(arr)
min_val = np.min(arr)
max_val = np.max(arr)
std_val = np.std(arr)

print("\nStatistical Functions on arr:")
print("Mean:", mean_val)
print("Median:", median_val)
print("Minimum:", min_val)
print("Maximum:", max_val)
print("Standard Deviation:", std_val)

# -------------------------------
# 7. Additional Functions
# -------------------------------

# Identity matrix
identity = np.eye(3)
print("\nIdentity Matrix (3x3):\n", identity)

# Zeros like another array
zeros_like_arr = np.zeros_like(arr)
print("\nZeros like arr:\n", zeros_like_arr)

# Ones like another array
ones_like_arr = np.ones_like(arr)
print("\nOnes like arr:\n", ones_like_arr)

# Array slicing and indexing
print("\nSlicing arr - First row:\n", arr[0])
print("Element at position [1][1]:", arr[1][1])
