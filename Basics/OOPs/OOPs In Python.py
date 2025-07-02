class Employee:
    def __init__(self, name, email, salary): # constructor dunder magic method
        self.name = name
        self.email = email
        self.salary = salary

    def employee_details(self):
        print(f'The details of the employee named {self.name} are: ')
        print('Name: ', self.name)
        print('Email: ', self.email)
        print('Salary: ', self.salary)

    def check_salary(self, other):
        if self.salary > other.salary:
            print(f'{self.name} has more salary than {other.name}')
        else:
            print(f'{other.name} has got more salary than {self.name}')
# self is the default parameter replaced by the current calling object
# class has no memory
# object occupies memory -> Heap memory
# PrepInsta Top 100 codes


e1 = Employee('Vinay', 'vinay@gmail.com', 35000)
e2 = Employee('Vijay', 'vijay@gmail.com', 36000)
e1.employee_details()
e2.employee_details()
e1.check_salary(e1)



