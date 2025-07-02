a = 2  # 0010 pseudo codes
b = 4  # 0100
#        0110
"""
Same - 0
Diff - 1
5 - 0101
~5- 1010 = 10
Compiler's memory cannot store negative values,
so, take the absolute value of -6 -> 6.
6 ->       0110
1's c  ->  1001
Add 1  ->  0001
1's c + 1 = 2's compliment. So, bitwise not is also 
called double negation or negation of 2.

"""

print(~-50)
