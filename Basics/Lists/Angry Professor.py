n = 5 # total strength of a class
k = 3 # minimum strength required

# entry time of students:
a = [-1, -3, 4, 2, 0]

b = [ele for ele in a if ele <= 0]

if len(b) < k:
    print('Class Cancelled...!!')
else:
    print('Class will continue..!!')

