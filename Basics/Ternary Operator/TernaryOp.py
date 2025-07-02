# Ternary Operator
# (condition) ? tValue : fValue; // C, C++, Java

"""
Ternary Operator is actually a simplified version of the if-else statement.
This operator evaluates a statement and then performs an action based on
whether the result of the given expression is True or False.
"""
# How to find the max/min values using the Ternary Operator

v1, v2 = 100, 200
min_no = v1 if v1 < v2 else v2
max_no = v1 if v1 > v2 else v2
print(f'Max Number is {max_no}')  # 200
print(f'Min Number is {min_no}')  # 100

