str1 = 'study'
str2 = 'dusty'
"The quick brown fox jumps over the lazy dog"
"education, cauliflower Mozambique"
s1 = sorted(str1, reverse=True)
s2 = sorted(str2, reverse=True)

print(type(s1), type(s2))
print(s1, s2)

if s1 == s2:
    print('Anagrams')
else:
    print('Not Anagrams')

