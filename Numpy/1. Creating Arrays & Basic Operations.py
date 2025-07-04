import numpy as np

# Creating a NumPy array from a list
arr = np.array([1, 2, 3, 4])

"""
This creates a 1D array:
[1 2 3 4]
"""

print("Original Array:", arr)

# Element-wise square
squared = np.square(arr)

"""
np.square() performs element-wise squaring:
[1 4 9 16]
"""

print("Squared:", squared)

# Mean of the array
print("Mean:", np.mean(arr))
