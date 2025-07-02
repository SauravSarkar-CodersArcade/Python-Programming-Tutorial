import json
myDict = {
    "students" : [
        {
            'name' : 'Vinay',
            'rollNo': 23,
            'marks': 56
        },
        {
            'name' : 'Vijay',
            'rollNo': 24,
            'marks': 58
        },
        {
            'name' : 'Vishwas',
            'rollNo': 25,
            'marks': 50
        }
    ]
}

json_string = json.dumps(myDict, indent=4)

with open('students.json', 'w') as f:
    f.write(json_string)