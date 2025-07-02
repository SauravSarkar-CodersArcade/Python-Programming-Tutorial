import xml.etree.ElementTree as ET

tree = ET.parse('trainers.xml')
root = tree.getroot()
# print(ET.tostring(root))
# company = root.get('com')
# print("Company name = {val}".format(val=company))
#
# # Set 'established' attribute
#
# root.set('established', '03/01/2021')
# print(root.attrib)
#
# # Save the updated xml file
# tree.write('trainers.xml')

# # Add an empID attribute to each trainer
# empID = 1001
#
# for trainer in tree.findall('trainer'):
#     trainer.set('empID', str(empID))
#     empID += 1
#
# # Save the updated xml file
# tree.write('trainers.xml')

# Delete 'empID' attributes

# for trainer in tree.findall('trainer'):
#     del(trainer.attrib['empID'])
#
# tree.write('trainers.xml')

# Add a new trainer to the xml file
# Method 1: Using the fromstring() method
# new_trainer_1 = ET.fromstring('<trainer>Sachin H</trainer>')
# root.append(new_trainer_1)
# Method 2: Using the Element() constructor
# new_trainer_2 = ET.Element('trainer')
# new_trainer_2.text = 'Ujjwal K'
# root.append(new_trainer_2)

# Let's add the empIDs once more using paths:
# for (empID, trainer) in enumerate(root.findall('trainer')):
#     trainer.set('empID', str(1001+empID))

# Select trainer 1005 by using the xpath
# trainer = root.find(".//trainer[@empID='1004']")
# print(trainer.text)
# tree.write('trainers.xml')



