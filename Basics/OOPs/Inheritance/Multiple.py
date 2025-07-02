class Mammal:
    def mammal_info(self):
        print('Mammals can give direct birth.')


class WingedAnimals:
    def winged_animal_info(self):
        print('Winged animals can flapp their wings..!!')


class Bat(Mammal, WingedAnimals):
    pass


b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()