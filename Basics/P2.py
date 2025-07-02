name = 'Reva'
student_count = 20000

# Type Conversion:
"""
1. Implicit - Automatic - Compiler 
2. Explicit - Manual - User
"""
# Addition of strings is called concatenation
print(name + ' university has a strength of ' + str(student_count) + ' students.')
print(name, 'university has a strength of', student_count, 'students.')

# Formatted Strings:
"""
1. 'f' formatter
2. format() function 
{} - > Placeholder -> It holds the value of the variable
"""
print(f'{name} university has a strength of {student_count} students.')
print('{4} university has a strength of {1} students.'.format(name, student_count, 30000, 'RV', 'BMS'))


# a = 10
# b = 3
# c = a/b # 3.3333
# print(c)
# print(type(a), type(b), type(c))