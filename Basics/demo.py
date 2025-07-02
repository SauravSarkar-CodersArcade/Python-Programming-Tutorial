name = 'Neha'
age = 20
print('My name is ' + name + ' and my age is ' + str(age))

"""
Formatted Strings:
1. formatter 'f'
2. format()
{} -> Place holder
"""
print(f'My name is {name} and my age is {age}')
print('My name is {2} and my age is {3}'.format(name, age, 'Ben', 32))

data = 'AVER'
print(data[::-1])

n1 = 'dusty'
n2 = 'study'
n3 = 'silent'
n4 = 'listen'
d1 = sorted(n3, reverse=True)
d2 = sorted(n4, reverse=True)
print(d1, d2)
if sorted(n3) == sorted(n4, reverse=True):
    print('Anagrams')
else:
    print('Not Anagrams')

# Pangram :The quick brown fox jumps over the lazy dog
# Education / Cauliflower / Mozambique

names = ['Ben', 'John', 'Smith', 'Parker']
print(max(names, key=len))


