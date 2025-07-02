str1 = 'dormitory'
str2 = 'dirty room'
# Sorted function returns a list of strings in alphabetical order

# str1_f = sorted(str1, reverse=True) # z-a
# str2_f = sorted(str2, reverse=True)
#
# print(str1_f)
# print(str2_f)
# if len(str1) == len(str2):
#     if sorted(str1) == sorted(str2):
#         print('Anagrams')
#     else:
#         print('Not Anagrams')
# else:
#     print('Not Anagrams')


alphabets = 'abcdefghijklmnopqrstuvwxyz'

s1 = []
s2 = []

for i in alphabets:
    if i in str1:
        s1.append(i)
    if i in str2:
        s2.append(i)

print(s1, s2)

if s1 == s2:
    print('Anagrams')
else:
    print('Not Anagrams')



