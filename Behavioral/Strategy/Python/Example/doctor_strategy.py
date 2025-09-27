from abc import ABC, abstractmethod

class DoctorStrategy(ABC):
    @abstractmethod
    def examine(self, patient_id):
        pass

class InpatientDoctor(DoctorStrategy):
    def examine(self, patient_id):
        return f"Inpatient Doctor: Khám bệnh nhân {patient_id} nằm viện"

class OutpatientDoctor(DoctorStrategy):
    def examine(self, patient_id):
        return f"Outpatient Doctor: Khám bệnh nhân {patient_id} ngoại trú"

class EmergencyDoctor(DoctorStrategy):
    def examine(self, patient_id):
        return f"Emergency Doctor: Cấp cứu bệnh nhân {patient_id}"

class Department:
    def __init__(self):
        self.doctor_strategy = None

    def assign_doctor(self, strategy: DoctorStrategy):
        self.doctor_strategy = strategy

    def handle_patient(self, patient_id):
        if not self.doctor_strategy:
            return "Chưa có bác sĩ được phân công"
        return self.doctor_strategy.examine(patient_id)