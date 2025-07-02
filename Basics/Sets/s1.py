# creating a set
s1 = {1,2,3,4,5}
s2 = {}
print(type(s1), type(s2))

emptySet = set()
print(type(emptySet))

mixedSet = {1.0, "Hello", (1,2,3)}
print(mixedSet)
# Converting a list into a set
set_with_lists = set([1,2,3])
print(type(set_with_lists))
print(set_with_lists)

set4 = set()
set4.update([9,12])
set4.update((3,5))
set4.update('REVA')
set4.update(('INDIA','BHARAT'))
print(set4)


