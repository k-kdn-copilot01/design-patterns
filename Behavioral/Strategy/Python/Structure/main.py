from strategy import InpatientStrategy, OutpatientStrategy, EmergencyStrategy, Hospital

if __name__ == "__main__":
    # Tạo hospital với strategy mặc định
    hospital = Hospital(InpatientStrategy())
    
    # Demo các chiến lược điều trị
    print("=== Nội trú ===")
    print(hospital.admit_patient("BN001"))
    
    print("\n=== Ngoại trú ===")
    hospital.set_treatment_strategy(OutpatientStrategy())
    print(hospital.admit_patient("BN002"))
    
    print("\n=== Cấp cứu ===")
    hospital.set_treatment_strategy(EmergencyStrategy())
    print(hospital.admit_patient("BN003"))