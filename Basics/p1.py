# data = [1,2,3,4,5]
# data1 = [5,6,7,8]
# for i in data1:
#     if i not in data:
#         print(i)

a = 100
b = 100
print(hex(id(a)))
print(hex(id(b)))

if a is not b:
    print('Diff id')
else:
    print('Same id')