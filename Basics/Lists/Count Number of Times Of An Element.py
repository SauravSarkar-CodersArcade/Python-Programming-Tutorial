# Program to check number of times an element occurred in list
print('Enter the number of elements: ')
n = int(input())

a = []
for i in range(n):
    print('Enter Element {0}: '.format(i+1))
    ele = int(input())
    a.append(ele)

print('Elements of list are: ', a)
print('Enter element to be searched: ')
key = int(input())

res = a.count(key)

if res == 0:
    print('Element not found.')
else:
    print('Element present {0} times.'.format(res))

