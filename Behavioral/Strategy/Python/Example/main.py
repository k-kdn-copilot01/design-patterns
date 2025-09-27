from doctor_strategy import Department, InpatientDoctor, OutpatientDoctor, EmergencyDoctor

if __name__ == "__main__":
    # Tạo khoa
    department = Department()
    
    # Demo phân công bác sĩ theo từng trường hợp
    patients = [
        ("BN001", "nội trú", InpatientDoctor()),
        ("BN002", "ngoại trú", OutpatientDoctor()),
        ("BN003", "cấp cứu", EmergencyDoctor())
    ]
    
    for patient_id, case_type, doctor_strategy in patients:
        department.assign_doctor(doctor_strategy)
        result = department.handle_patient(patient_id)
        print(f"{case_type.upper()}: {result}")