import json
import os

file_name = "medical_records.json"

def get_records():
    if not os.path.exists(file_name):
        return []

    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return []

def save_records(records):
    with open(file_name, "w") as file:
        json.dump(records, file, indent=4)

def add_record():
    records = get_records()

    rid = input("Enter record ID: ")
    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    date = input("Enter date: ")
    symptoms = input("Enter symptoms: ")
    diagnosis = input("Enter diagnosis: ")
    medicine = input("Enter prescribed medicine: ")

    record = {
        "id": rid,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "symptoms": symptoms,
        "diagnosis": diagnosis,
        "medicine": medicine
    }

    records.append(record)
    save_records(records)
    print("Medical record saved.")

def show_records():
    records = get_records()

    if not records:
        print("No medical records found.")
        return

    print("\n----- Medical Records -----")

    for record in records:
        print("\nRecord ID   :", record["id"])
        print("Patient ID  :", record["patient_id"])
        print("Doctor ID   :", record["doctor_id"])
        print("Date        :", record["date"])
        print("Symptoms    :", record["symptoms"])
        print("Diagnosis   :", record["diagnosis"])
        print("Medicine    :", record["medicine"])

def patient_history():
    records = get_records()
    pid = input("Enter patient ID: ")
    found = False

    for record in records:
        if record["patient_id"] == pid:
            print("\nDate      :", record["date"])
            print("Doctor ID :", record["doctor_id"])
            print("Symptoms  :", record["symptoms"])
            print("Diagnosis :", record["diagnosis"])
            print("Medicine  :", record["medicine"])
            found = True

    if not found:
        print("No medical history found.")

def medical_menu():
    while True:
        print("\n===== MEDICAL RECORDS =====")
        print("1. Add medical record")
        print("2. Show all records")
        print("3. Patient history")
        print("4. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            patient_history()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")