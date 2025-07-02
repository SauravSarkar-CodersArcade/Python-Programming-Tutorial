# 3.10 or python 10 2021 (Match case)

server_code = 100

match server_code:
    case 200:
        print('Good request')
    case 400:
        print('Bad request')
    case other:
        print('Something else that is bad happened')
