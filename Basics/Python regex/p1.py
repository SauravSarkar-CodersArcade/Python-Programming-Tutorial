import re
txt = 'The rains in Bangalore'

x = re.search("^The.*Bangalore$", txt)

if x:
    print('Match Found...!!!')
else:
    print('No Match')

txt1 = "The rain in Terrain in Spain"
y = re.findall("z", txt1)
print(y)

