import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication using @ operator or np.dot()
product = a @ b

"""
Matrix multiplication:
[[1*5 + 2*7, 1*6 + 2*8],
 [3*5 + 4*7, 3*6 + 4*8]]
= [[19, 22],
   [43, 50]]
"""

print("Matrix Product:\n", product)
