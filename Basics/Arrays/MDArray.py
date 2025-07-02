# Array of arrays
# rows and columns
# 3 rows 4 columns
# Jagged Array ?
# A md array where no of elements in each row is different
# Write a program to demonstrate iteration over
# a jagged array
md_array = [[1,2,3,4,5,6,7,8],
            [5,6,7,8],
            [9,8,7]]

# i is each row
# each row is an array, so, len(array)
for i in range(len(md_array)):
    for j in range(len(md_array[i])):
        print(md_array[i][j], end=' ')
    print()

for i in md_array:
    for j in i:
        print(j, end=' ')
    print()

