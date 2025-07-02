marksList = [
            ['Language', 56],
            ['Mathematics', 45],
            ['Science', 76]
            ]

for ele in marksList:
    # print('marks scored in', ele[0], 'is', ele[1])
    print(f'Marks scored in {ele[0]} is {ele[1]}.')

# area variables in a house: (in square metres)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists:
house = [['hallway', hall],
         ['kitchen', kit],
         ['living room', liv],
         ['bedroom', bed],
         ['bathroom', bath]]

# print the entire house:
print(house)
print(house[0])
print(house[1][0])

