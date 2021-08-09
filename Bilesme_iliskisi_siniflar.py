"""
Birleşme ilişisi sınıflar
"""

class Doctor:
    pass

class Hospital:
    def __init__(self, doctors = ()):
        self.doctors = list(doctors)
    
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        
    def remove_doctors(self, doctor):
        self.doctors.remove(doctor)


hospital_x = Hospital()
doctor_a = Doctor()
hospital_x.add_doctor(doctor_a)
doctor_b = Doctor()
hospital_x.add_doctor(doctor_b)

hospital_y = Hospital()
hospital_y.add_doctor(doctor_a) 
