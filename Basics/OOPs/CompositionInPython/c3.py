class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.emp_salary = Salary(pay, bonus)

    def total_salary(self):
        return self.emp_salary.annual_salary()


e1 = Employee('Max', 34, 25000, 12000)
print(f'The total salary of {e1.name} is {e1.total_salary()}')
