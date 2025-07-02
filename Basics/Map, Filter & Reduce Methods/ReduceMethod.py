from functools import reduce
numbers = [1, 2, 3, 4, 5]
# 1x2x3x4x5 = 120
product = reduce(lambda x, y: x*y, numbers)
print(product)