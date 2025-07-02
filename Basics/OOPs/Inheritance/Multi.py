class SimpleCalculator:
    def addition(self, a, b):
        print(f'The sum of {a} and {b} is {a+b}')


class AdvancedCalculator(SimpleCalculator):
    def subtraction(self, a, b):
        print(f'The difference of {a} and {b} is {a-b}')


class SuperAdvancedCalculator(AdvancedCalculator):
    def division(self, a, b):
        print(f'Division of {a} by {b} gives {a/b}')

    def product(self, a, b):
        print(f'The product of {a} and {b} is {a*b}')


print('-----------------------------------------------')
c1 = SimpleCalculator()
c1.addition(10,20)
print('-----------------------------------------------')
c2 = AdvancedCalculator()
c2.addition(12, 23)
c2.subtraction(20, 10)
print('-----------------------------------------------')
c3 = SuperAdvancedCalculator()
c3.addition(10,20)
c3.subtraction(20,10)
c3.division(20, 5)
c3.product(100, 2)
print('-----------------------------------------------')