class Student:
    def __init__(self, name, rollNo, email, t_marks):
        self.name = name
        self.rollNo = rollNo
        self.email = email
        self.t_marks = t_marks

    def student_details(self):
        print(f'The details of the student with name {self.name} are: ')
        print(f'Name: {self.name}')
        print(f'Roll number: {self.rollNo}')
        print(f'Email Address: {self.email}')
        print(f'Total marks: {self.t_marks}')

    def check_marks(self, other):
        if self.t_marks > other.t_marks:
            print(f'{self.name} has more marks than {other.name}.')
        else:
            print(f'{other.name} has more marks than {self.name}.')


s1 = Student('Sameer', 101, 'sameer@gmail.com', 565)
s2 = Student('Raman', 102, 'raman@gmail.com', 548)

s1.student_details()
s2.student_details()

s1.check_marks(s2)


class Demo:
    pass


d = Demo()
d.name = 'Sam'
