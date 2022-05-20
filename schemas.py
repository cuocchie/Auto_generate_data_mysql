import random
from names import get_full_name
from generator import get_instruction, get_med_list, get_random_station, random_date, get_disease, random_phone_number


class Table:

    def __init__(self, tablename, id) -> None:
        self.tablename = tablename
        self.id = id
        pass


class Station(Table):

    def __init__(self) -> None:
        super().__init__('station', 'station_id')

        self.name = 'name'
        self.description = 'description'

    def generate(index):
        station_list = ['Lab Station', 'Shelving Station', 'Secure Sation']
        description = ['Prescriptions for drugs that must be formulated (made on-site)',\
            'prescriptions for off-the-shelf drugs',\
            'prescriptions for narcotics']

        return (station_list[index], description[index])

    def insert(self, index):
        value = Station.generate(index)
        return value


class Pharmacist(Table):

    def __init__(self) -> None:
        super().__init__('pharmacist', 'pharmacist_id')

        self.name = 'name'
        self.telephone = 'telephone'
        self.station_id = 'station_id'

    def generate():
        return (get_full_name(),\
            f'0{random.randint(10**(9 - 1), (10**9) - 1)}',\
            random.randint(1, 3))

    def insert(self):
        value = Pharmacist.generate()
        return value


class Patient(Table):

    def __init__(self) -> None:
        super().__init__('patient', 'patient_id')

        self.name = 'name'
        self.telephone = 'telephone'

    def generate():
        return (get_full_name(),\
            random_phone_number()
        )

    def insert(self):
        value = Patient.generate()
        return value


class File(Table):

    def __init__(self) -> None:
        super().__init__('file', 'file_id')

        self.date = 'date'
        self.diagnosis = 'diagnosis'
        self.patient_id = 'patient_id'

    def generate(patient_id):
        return (random_date("2021/1/1", "2022/5/1"),\
            get_disease(),
            patient_id
        )

    def insert(self, patient_id):
        value = File.generate(patient_id)
        return value


class Doctor(Table):

    def __init__(self) -> None:
        super().__init__('doctor', 'doctor_id')

        self.name = 'name'
        self.telephone = 'telephone'

    def generate():
        return (get_full_name(),\
            random_phone_number()
        )

    def insert(self):
        value = Doctor.generate()
        return value


class Prescription(Table):

    def __init__(self) -> None:
        super().__init__('prescription', 'pres_id')

        self.is_valid = 'is_valid'
        self.special_instruction = 'special_instruction'
        self.station = 'station'
        self.patient_id = 'patient_id'
        self.doctor_id = 'doctor_id'
        self.pharmacist_id = 'pharmacist_id'

    def generate(patient_id):
        return (random.randint(0, 1),\
            get_instruction(),\
            get_random_station(), \
            patient_id, \
            random.randint(1, 35), \
            random.randint(1, 30)
        )

    def insert(self, patient_id):
        value = Prescription.generate(patient_id)
        return value


class Medicine(Table):

    def __init__(self) -> None:
        super().__init__('medicine', 'medicine_id')

        self.name = 'name'
        self.price = 'price'
        self.description = 'description'

    def generate(med_index):
        return (get_med_list()[med_index], \
            random.randint(50, 9000),
            'None'
        )

    def insert(self, med_index):
        value = Medicine.generate(med_index)
        return value


class Medicine_included(Table):

    def __init__(self) -> None:
        super().__init__('medicine_included', 'id')

        self.pres_id = 'pres_id'
        self.medicine_id = 'medicine_id'
        self.amount = 'amount'

    def generate(pres_id):
        return (pres_id, \
            random.randint(1, 67),
            random.randint(1, 20)
        )

    def insert(self, pres_id):
        value = Medicine_included.generate(pres_id)
        return value