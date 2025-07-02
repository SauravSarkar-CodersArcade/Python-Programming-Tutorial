# Arbitrary keyword arguments
# in the parameter we write ** before
# We access the arguments using : parameter['key']

def name(**s):
    print('The name of the student is: ', s['s2'])


name(s2='Sam', s1='Ben', s3='John')
