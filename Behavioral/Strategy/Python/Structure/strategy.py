from abc import ABC, abstractmethod

class TreatmentStrategy(ABC):
    @abstractmethod
    def treat(self, patient_id):
        pass

class InpatientStrategy(TreatmentStrategy):
    def treat(self, patient_id):
        return f"Inpatient treatment for {patient_id}: Khám chi tiết, nằm viện theo dõi"

class OutpatientStrategy(TreatmentStrategy):
    def treat(self, patient_id):
        return f"Outpatient treatment for {patient_id}: Khám nhanh, không nằm viện"

class EmergencyStrategy(TreatmentStrategy):
    def treat(self, patient_id):
        return f"Emergency treatment for {patient_id}: Cấp cứu khẩn cấp, ưu tiên cao"

class Hospital:
    def __init__(self, strategy: TreatmentStrategy):
        self._strategy = strategy

    def set_treatment_strategy(self, strategy: TreatmentStrategy):
        self._strategy = strategy

    def admit_patient(self, patient_id):
        return self._strategy.treat(patient_id)
