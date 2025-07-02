# Without the Walrus Operator:
# user_input = ''
# if len(user_input) > 0:
#     print(f'The input value is {user_input}.')
# else:
#     print('No input was given.')

# With Walrus Operator:

if (user_input := input('Enter a value: ')) != "":
    print(f'The input value is: {user_input}')
else:
    print('No input was given.')
