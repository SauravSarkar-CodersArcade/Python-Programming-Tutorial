"""
If we are not passing a 'name' argument, the function gets
the default value, but if we pass the 'name' argument then
the function does that particular operation.
"""


class Human:
    def greet_hello(self, name=None):
        if name is not None:
            print('Hi ' + name)
        else:
            print('Hello')


h = Human()
h.greet_hello('Sanjay')