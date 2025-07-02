class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1 = Student(95, 60)  # 105
s2 = Student(55, 78) # 133

# a = 10
# b = 20
# c = 'Hi'
# d = ' Hello'
# print(a+b)
# print(a.__gt__(b))
# print(a>b)
# print(c+d)
s3 = s1+s2
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print('s1 has more marks than s2')
else:
    print('s2 has more marks than s1')

