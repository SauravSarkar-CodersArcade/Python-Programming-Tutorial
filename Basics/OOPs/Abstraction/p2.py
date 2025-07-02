from abc import ABC, abstractmethod


class Defence(ABC):
    @abstractmethod
    def area_of_operation(self):
        pass


class Army(Defence):
    def area_of_operation(self):
        print('Land, Air, Water...!!!')


class Navy(Defence):
    def area_of_operation(self):
        print('Generally Water...!!!')


class AirForce(Defence):
    def area_of_operation(self):
        print('Generally Air...!!!')


a1 = Army()
n1 = Navy()
a3 = AirForce()
print(f'Army: {a1.area_of_operation()}')
print(f'Navy: {n1.area_of_operation()}')
print(f'Air Force: {a3.area_of_operation()}')
