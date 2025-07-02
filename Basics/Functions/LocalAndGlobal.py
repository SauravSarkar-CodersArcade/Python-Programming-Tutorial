x = 200 # BMTC global - accessible to everyone


def f1():
    x = 10 # Your private vehicle local - accessible inside function
    print('The value of x is:', x)


def f2():
    x = 20 # Your private vehicle local - accessible inside function
    print('The value of x is:', x)
    f1()


f2()
