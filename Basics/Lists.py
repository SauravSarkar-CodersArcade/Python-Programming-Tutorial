data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List Comprehension
odd = [ele for ele in data if ele % 2 != 0]
even = [elem for elem in data if elem % 2 == 0]

# print(odd)
# print(even)
for i in data:
    for j in 'abc':
        print(i, j, end=' ')
    print()