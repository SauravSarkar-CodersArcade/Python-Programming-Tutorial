# Without Walrus Operator
myList = [1, 2, 3, 4, 5]
list_length = len(myList)
if list_length > 3:
    print(f"The list is longer than 3 elements: {myList}")
else:
    print("My list is not longer than 3 elements.")

# With Walrus Operator

if (length := len(myList)) > 3:
    print(f'My list is longer than 3 elements and length is: {length} : {myList}')
else:
    print("My list is not longer than 3 elements.")
