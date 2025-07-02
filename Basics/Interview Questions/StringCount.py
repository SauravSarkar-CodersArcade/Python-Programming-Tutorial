data = input('Enter the desired string: ')

print('The length of the string is: ', len(data))

digits = 0
upper = 0
lower = 0
space = 0

for ele in data:
    if ele.isdigit():
        digits += 1
    if ele.isupper():
        upper += 1
    if ele.islower():
        lower += 1
    if ele.isspace():
        space += 1

print('the string contains {0} digits'.format(digits))
print('the string contains {0} Upper cases'.format(upper))
print('the string contains {0} Lower cases'.format(lower))
print('the string contains {0} White spaces'.format(space))

