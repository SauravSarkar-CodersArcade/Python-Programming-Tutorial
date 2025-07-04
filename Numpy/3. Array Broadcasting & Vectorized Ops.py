import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Add two arrays element-wise
c = a + b

"""
Broadcasting allows you to add arrays of the same shape:
[1+10, 2+20, 3+30] => [11 22 33]
"""

print("a + b =", c)

# Multiply with scalar
print("a * 5 =", a * 5)
