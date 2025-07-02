import re

text = '''
Elon Musk's phone number is 9919822123, call him if you have any questions on 
SpaceX. 
Tesla's revenue is 40 billion.
Tesla's CFO's number is (999)-333-7777 
'''
pattern = '\d\d\d\d\d\d\d\d\d\d'
pattern1 = '\d{10}'
pattern2 = '\(\d{3}\)-\d{3}-\d{4}'
pattern3 = '\d\d\d\d\d\d\d\d\d\d|\d{10}|\(\d{3}\)-\d{3}-\d{4}'

"""
^ -> beginning
$ -> end
\ -> to select a character
d - digits
{2} - no of digits
.* everything in the middle
"""
matches = re.findall(pattern3, text)
print(matches)
