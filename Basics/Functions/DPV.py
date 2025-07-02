# Default parameter value
# If we pass arguments, default is skipped, or else
# default is considered.

def favourite_subject(fav='Mathematics'):
    print('My favourite subject is: ', fav)


favourite_subject('Machines')
favourite_subject('C++')
favourite_subject('Java')
favourite_subject('Python')
favourite_subject()
# pass statement is used to skip a function
def login():
    pass

