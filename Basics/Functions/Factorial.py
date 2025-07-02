# 0! = 1
# 1! = 1
# -1 ! = not defined
# 5 = 5x4x3x2x1 = 120
def factorial(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)     # 5 x 4!  4 x 3! 3 X 2!


n = int(input('Enter the number: '))
res = factorial(n)
print(res)


# fact = 1
#
# if n < 0:
#     print('Factorial of negative numbers is undefined.')
# elif n == 0 or n == 1:
#     print(f'Factorial of {n} is {fact}')
# else:
#     for i in range(1, n+1):
#         fact = fact * i
#     print(f'The factorial of {n} is {fact}')

