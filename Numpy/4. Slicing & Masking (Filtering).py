import numpy as np

arr = np.array([5, 10, 15, 20, 25, 30])

# Slicing from index 1 to 4 (exclusive)
print("Slice arr[1:4]:", arr[1:4])

# Boolean masking: Get values > 15
filtered = arr[arr > 15]

"""
arr > 15 returns a boolean array:
[False False False  True  True  True]
Which selects the elements where condition is True:
[20 25 30]
"""

print("Filtered:", filtered)
