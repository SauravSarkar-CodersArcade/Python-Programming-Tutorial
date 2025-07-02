# 3.10 2021 Python version 10 Match case
status_code = 100

match status_code:
    case 200:
        print('good')
    case 400:
        print('bad')
    case other:
        print('It is also bad')