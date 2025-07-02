class Animal:
    def eat(self):
        print('Eating...!!!')

    def sleep(self):
        print('Sleeping...!!!')


class Cat(Animal):
    def sound(self):
        print('I am a cat. I meow...!!!')

    def run(self):
        print('I am a cat. I run fast...!!!')


a1 = Animal()
a1.sleep()
a1.eat()
c1 = Cat()
c1.sleep()
c1.eat()
c1.run()
c1.sound()
