# empty tuple
my_tuple = ()
print(my_tuple)

# tuple with integers
my_tuple = (1,2,3)
print(my_tuple)

# mixed tuple
my_tuple1 = (1, 'hello', 3.4)
print(my_tuple1)

# nested tuple
my_tup_nest = ('mouse', [8,4,6], (1,2,3))
print(my_tup_nest)

# tuple can be created without parentheses also :
"""
Q. Important question: What is tuple packing?
Ans: if we do not use the brackets to create the tuple,
it is called tuple packing. 
"""
t1 = 3,4.6, 'cat'
print(type(t1))

t2 = ('hello',)
t3 = ('Hi') # it is a string because no comma is added
print(type(t2))

t4 = ('Vinay', [8,4,2], (5,6,7))
print(t4)

"""
Unlike lists, tuples are immutable.
This means item assignment is not possible once the elements
have been declared.
But, if the element itself is a mutable datatype like list, 
it's nested items can be changed. 
"""

t4[1][1] = 32
print(t4)

