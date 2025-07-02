data = [1,2,3,4,5]
# end=' ' means the control stays on the same line
# breakpoint - debug our code
"""
The working principle of neater for loop:
first the innermost loop has to complete, then the 
control goes to the outer for loop for 
the next iteration.
"""

for i in data:
    for j in 'abc':
        print(i,j, end=' ')
    print()