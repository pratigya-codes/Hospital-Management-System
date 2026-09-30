import json
import os

file_name = "doctors.json"

def get_doctors():
    if not os.path.isfile(file_name):
        return []
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except Exception:
        return []

def save_doctors(doctors):
    with open(file_name, "w") as file:
        json.dump(doctors, file, indent=4)

def add_doctor():
    doctors = get_doctors()
    did = input("Enter doctor ID: ").strip()

    for doctor in doctors:
        if doctor["id"] == did:
            print("Doctor ID already exists.")
            return

    name = input("Enter doctor name: ").strip()
    specialization = input("Enter specialization: ").strip()
    department = input("Enter department: ").strip()
    phone = input("Enter phone number: ").strip()
    timing = input("Enter available timing: ").strip()

    doctor = {
        "id": did,
        "name": name,
        "specialization": specialization,
        "department": department,
        "phone": phone,
        "timing": timing
    }
    doctors.append(doctor)
    save_doctors(doctors)
    print("Doctor added successfully.")

def show_doctors():
    doctors = get_doctors()
    if not doctors:
        print("No doctor records available.")
        return

    print("\n----- Doctor List -----")
    for doctor in doctors:
        print(f"\nDoctor ID      : {doctor['id']}")
        print(f"Name           : {doctor['name']}")
        print(f"Specialization : {doctor['specialization']}")
        print(f"Department     : {doctor['department']}")
        print(f"Phone          : {doctor['phone']}")
        print(f"Available time : {doctor['timing']}")

def search_doctor():
    doctors = get_doctors()
    value = input("Enter doctor ID or name: ").strip().lower()

    for doctor in doctors:
        if doctor["id"].lower() == value or value in doctor["name"].lower():
            print("\nDoctor found")
            print(f"ID             : {doctor['id']}")
            print(f"Name           : {doctor['name']}")
            print(f"Specialization : {doctor['specialization']}")
            print(f"Department     : {doctor['department']}")
            print(f"Phone          : {doctor['phone']}")
            print(f"Available time : {doctor['timing']}")
            return

    print("Doctor not found.")

def update_doctor():
    doctors = get_doctors()
    did = input("Enter doctor ID: ").strip()

    for doctor in doctors:
        if doctor["id"] == did:
            name = input("New name: ").strip()
            department = input("New department: ").strip()
            timing = input("New available timing: ").strip()

            if name:
                doctor["name"] = name
            if department:
                doctor["department"] = department
            if timing:
                doctor["timing"] = timing

            save_doctors(doctors)
            print("Doctor details updated.")
            return

    print("Doctor not found.")

def delete_doctor():
    doctors = get_doctors()
    did = input("Enter doctor ID: ").strip()

    for doctor in doctors:
        if doctor["id"] == did:
            doctors.remove(doctor)
            save_doctors(doctors)
            print("Doctor deleted.")
            return

    print("Doctor not found.")

def doctor_menu():
    while True:
        print("\n===== DOCTOR MANAGEMENT =====")
        print("1. Add doctor")
        print("2. Show doctors")
        print("3. Search doctor")
        print("4. Update doctor")
        print("5. Delete doctor")
        print("6. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_doctor()
        elif choice == "2":
            show_doctors()
        elif choice == "3":
            search_doctor()
        elif choice == "4":
            update_doctor()
        elif choice == "5":
            delete_doctor()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")