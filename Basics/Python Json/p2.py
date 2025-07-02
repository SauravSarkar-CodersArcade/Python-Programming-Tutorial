import json

with open('students.json', 'r') as f:
    json_object = json.loads(f.read())
    f.read()


print(json_object)
print(json_object['students'][0])
print(json_object['students'][2]['name'])