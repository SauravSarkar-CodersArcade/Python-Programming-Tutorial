import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction
# print(dir(ET))
print('----------------------------------------')
# Display all the classes in ElementTree Module
for (name, member) in getmembers(ET, isclass):
    if not name.startswith("_"):
        print(name)
print('----------------------------------------')
# Display all the functions in ElementTree Module
for (name, member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name)
print('----------------------------------------')




