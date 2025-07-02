from a2 import *


class Patient:
    def __init__(self, name, age, doa, disease, info):
        self.name = name
        self.age = age
        self.doa = doa
        self.disease = disease
        self.admission_info = info

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


admission_info = Information('B', 2, 202, 5)
p1 = Patient('XYZ', 23, '21/11/22', 'Malaria', admission_info)
p1.patientDetails()
