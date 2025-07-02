from c2 import *


class Patient:
    def __init__(self, name, age, doa, disease, block, floor, room, bed):
        self.name = name
        self.age = age
        self.doa = doa
        self.disease = disease
        self.admission_info = Information(block, floor, room, bed)

    def patientDetails(self):
        print(f'The registration and admission details of the patient {self.name} are as follows: ')
        print(f'Patient Name: \t\t{self.name}')
        print(f'Patient age: \t\t{self.age}')
        print(f'Date of Arrival: \t{self.doa}')
        print(f'Disease: \t\t\t{self.disease}')
        print(f'Block Number: \t\t{self.admission_info.block}')
        print(f'Floor Number: \t\t{self.admission_info.floor}')
        print(f'Room Number: \t\t{self.admission_info.room}')
        print(f'Bed Number: \t\t{self.admission_info.bed}')


p1 = Patient('ABC', 24, '17/11/22', 'SARS-Covid-19', 'A', 5, 507, 4)
p1.patientDetails()
