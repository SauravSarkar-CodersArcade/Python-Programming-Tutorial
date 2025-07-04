import numpy as np

# Creating a 2x3 matrix
matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])

"""
Matrix:
[[10 20 30]
 [40 50 60]]
"""

# Access element at 2nd row, 3rd column (60)
print("Element at [1][2]:", matrix[1][2])

# Access all elements from 1st row
print("First row:", matrix[0])
