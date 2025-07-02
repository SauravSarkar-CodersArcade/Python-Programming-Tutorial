cities = ['Bengaluru', 'Hyderabad', 'Chennai', 'Delhi', 'Goa']

print('Before Sorting: ')
print(cities)

cities.sort(reverse=True)
cities.sort(key=len)
print('After sorting: ')
print(cities)

a = [12,13,21,2,32,11]
print('Before Sorting: ')
print(a)
b = sorted(a)
print('After Sorting: ')
print(b)

# List in reverse :
c = [1,2,3,4,5]
print(c[::-1])
