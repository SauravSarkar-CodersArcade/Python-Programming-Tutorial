"""
As long as you yourself are not ready to learn, even god
can't make you learn...!!!
pep : Python Enhancement Proposal - It helps us to write better code
"""


class Car:
    def __init__(self, speed, color):
        # Making the data members private by using double underscores (__)
        self.__speed = speed
        self.__color = color
    # setters for setting the values

    def set_speed(self, value):
        self.__speed = value

    def set_color(self, col):
        self.__color = col
    # getters for getting the values

    def get_speed(self):
        return self.__speed

    def get_color(self):
        return self.__color


ferrari = Car(200, 'Red')
porsche = Car(195, 'Yellow')

ferrari.set_speed(250)
ferrari.set_color('Black')

print(ferrari.get_speed())
print(ferrari.get_color())
# print(ferrari.speed)  # Invalid/Access not provided




