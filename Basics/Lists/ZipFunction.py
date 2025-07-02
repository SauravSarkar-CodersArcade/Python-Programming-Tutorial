# zip() function takes iterables, makes iterator that
# aggregates elements based on the iterables passed, and
# returns an iterator of tuples.
rollNos = [1,2,3]
names = ['Sachin', 'Tanmay', 'Rahul']
marks = [56,67,78]

studentDetails = zip(rollNos, names, marks)
print(studentDetails)  # object

for record in studentDetails:
    print(record)



