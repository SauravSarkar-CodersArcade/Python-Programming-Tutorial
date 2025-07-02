"""
Union
Intersection
Difference
Symmetric Difference
"""
a = {1,2,3,4,5}
b = {4,5,6,7,8}

print('Union                = ', a | b)
print('Intersection         = ', a & b)
print('Difference           = ', a - b)
print('Symmetric Difference = ', a ^ b)


studentList = {'daniel', 'jason', 'sangeetha', 'uma',
               'amrutha', 'lohith', 'prasad', 'ashwini'}
placedStudents = ['uma', 'daniel', 'amrutha']

notPlacedStudents = set(studentList) - set(placedStudents)
print('Students yet to get job: \n', notPlacedStudents)

batsmen = ['virat', 'rahul', 'rohit', 'dhoni', 'pandya', 'jadeja']
bowlers = ['bhuvi', 'shami', 'pandya', 'jadeja', 'kuldeep']
allRounders = set(batsmen) - set(bowlers)
print("Batsmen: ", batsmen)
print('Bowlers: ', bowlers)
print('All Rounders: ', allRounders)

tcs = ['uma', 'danish', 'amrutha']
infosys = ['lohith', 'danish', 'ashwini']
wipro = ['samgeetha', 'jason', 'prasad', 'amrutha']

placedStudents = set(tcs) | set(infosys) | set(wipro)
print('Placed Students: ', placedStudents)
print("No of students placed: ", len(placedStudents))

# set functions : isdisjoint() issubset(), issuperset()
my_numbers = {1,2,3,4,5,6,7,8,9,10}
odd = {1,3,5,7,9}
even = {2,4,6,8,10}

print(odd.isdisjoint(even))  # True  (True if no matches)
print(my_numbers.issuperset(odd))  # True (True if set1 contains set2)
print(odd.issuperset(my_numbers))  # False (True if set1 contains set2)
print(odd.issubset(my_numbers))  # True (True if set1 is in set2)








