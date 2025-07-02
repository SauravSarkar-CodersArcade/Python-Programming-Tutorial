class Pycharm:
    def execute(self):
        print('Intellisense')
        print('Spell Check')
        print('Debugging')
        print('Compilation')


class VSCode:
    def execute(self):
        print('Spell Check')
        print('Debugging')
        print('Compilation')

class Laptop:
    def execute(self):
        ide.execute()


ide = Pycharm()
dell = Laptop()
dell.execute()