menu_items = {'Chicken Biryani': 120, 'Kebab': 60, 'Rumali Roti': 20}
# dict_name['key']

print(menu_items['Kebab'])
print(menu_items.keys())
print(menu_items.values())

# dict_name['new_key'] = value
menu_items['Kushka'] = 50
print(menu_items)

# del dict_name['key']
del menu_items['Kebab']
print(menu_items)

# Multiple Values for each key in a dictionary
majorCities = {'karnataka': ['bengaluru', 'mysore', 'hubli'],
               'tamil nadu':['chennai', 'coimbatore', 'madurai'],
               'maharashtra': ['mumbai', 'pune']}

print(majorCities)
print('\nCities of Tamil Nadu: ')
print(majorCities['tamil nadu'])

print('\nDifferent States: ')
print(majorCities.keys())

# Dictionary of Dictionaries
india = {'karnataka': {'capital':'bengaluru', 'population':46.77},
         'tamil nadu': {'capital':'chennai', 'population':66.03},
         'maharashtra': {'capital':'mumbai', 'population':80.62},
         'kerala': {'capital':'thiruvavanthapuram', 'population':5.084}
         }
# print out the capital of kerala:
print('Capital of kerala is', india['kerala']['capital'])

# create a sub-dictionary data
data = {'capital':'hyderabad', 'population':59.83}

# Add data to india under key 'telangana'

india['telangana'] = data
print(india)




