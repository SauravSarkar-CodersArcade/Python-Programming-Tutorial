class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.emp_salary = salary

    def total_salary(self):
        return self.emp_salary.annual_salary()


emp_salary = Salary(35000, 12000)
e1 = Employee('Max', 34, emp_salary)
print(f'The total salary of {e1.name} is {e1.total_salary()}')