passwords = ['REVA', 'EEE', '2021', 'PYTHON']
pwd = input('Enter the password: ')
# Default input by user in Python is String
if pwd.upper() in passwords:
    print('Access Granted')
else:
    print('Access Denied')