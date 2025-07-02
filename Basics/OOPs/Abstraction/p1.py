from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def show(self):  # Abstract method (Without a body)
        pass

    def display(self):  # Normal / Concrete Method (With a body)
        print('Method of class A')


class B(A):
    def show(self):
        print('Show class B')


b = B()
b.show()
b.display()
