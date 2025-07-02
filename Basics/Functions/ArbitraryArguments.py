# arbitrary arguments
# parameter is preceded by a * (asterisk)
# n number of arguments, accessed by index number
# index starts from 0 - (n-1)
def name(*s):
    print('The name of the student is: ', s[0])


name('Sam', 'Ben', 'John', 'Tim', 'Benny')
