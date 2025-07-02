def division(x):
    print(20/x)


try:
    division(10)
    division(z)
    division('Vinay')
    division(0)
    division(20)
    division(4)
except NameError:
    print('The var name is undefined.')
except ZeroDivisionError:
    print('Division by 0 is not valid.')
except TypeError:
    print('Invalid data types for division.')
finally:  # Release the resources
    print('I am the boss. I will always get executed.')

# The finally block is executed always no matter what happens to the code.

