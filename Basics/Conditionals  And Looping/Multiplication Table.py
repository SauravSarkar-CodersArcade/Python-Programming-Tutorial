# start, stop-1, step
n1 = int(input('Enter n1\n'))
n2 = int(input('Enter n2\n'))
for i in range(n1, n2 + 1):
    for j in range(1, 11):
        # print(i,'x',j,'=',i*j, end=' ')
        print(f'{i}x{j}={i * j}', end='\t')
    print()
