studMarksList = [
    [12,21,23], # 56
    [21,32,23], # 76
    [45,43,43]  # 131
]
rowSums = []
for ele in studMarksList:
    rowSums.append(sum(ele))
    print(rowSums[-1])

print(rowSums)
print('Total Sum: ', sum(rowSums))