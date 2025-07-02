# List Comprehension
nums = [12, 8, 3, 16]

new_nums = [num+1 for num in nums]

print(new_nums)
# SHA- 256
a = list(range(1,10))
print(a)
print(f'Odd numbers in {a} are: ')
b = [ele for ele in a if ele % 2 != 0]
print(b)