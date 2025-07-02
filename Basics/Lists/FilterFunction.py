numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
odd_numbers = filter(lambda x: x % 2 != 0, numbers)

print(list(even_numbers))
print(list(odd_numbers))

"""
Use the map() function and lambda to square all numbers
in a list
"""
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

"""
Capgemini 2022 December
Use the reduce() function to calculate the product 
of all elements in a list
"""
from functools import reduce
num = [1,2,3,4,5]
product = reduce(lambda x,y: x*y, num)
print(product)

