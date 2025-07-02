# Identity Matrix has diagonal elements 1
# Condition is whenever r == c print 1, else print 0
for r in range(4):
    for c in range(4):
        if r == c:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()