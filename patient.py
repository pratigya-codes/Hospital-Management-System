import json
import os

# Database file - keeping it simple with a json flat file for now
# TODO: migrate to sqlite if this gets too big, but works fine for testing
DATA_FILE = "patients.json"

def get_patients():
    # just checking if file exists, if not return empty list
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        f = open(DATA_FILE, "r")
        data = json.load(f)
        f.close() # manually closing cuz old habits die hard lol
        return data
    except Exception as e:
        # Sometimes the json gets corrupted if app crashes during write
        print("oops, error reading file:", e)
        return []

def save_patients(pat_list):
    # helper to save list back to json
    with open(DATA_FILE, "w") as f:
        json.dump(pat_list, f, indent=4)

def add_patient():
    patients = get_patients()

    pid = input("Enter patient ID: ")

    # check if already there
    exists = False
    for p in patients:
        if p["id"] == pid:
            exists = True
            break
            
    if exists:
        print("This patient ID already exists.")
        return

    name = input("Enter patient name: ")

    # age validation loop is annoying, let's just use try-except once
    try:
        age = int(input("Enter age: "))
    except:
        print("Age should be a number (like 25). Try again later.")
        return

    gender = input("Enter gender: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")

    # building the dict
    new_patient = {
        "id": pid,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "address": address
    }

    patients.append(new_patient)
    save_patients(patients)

    print("Patient added successfully.")

def show_patients():
    patients = get_patients()

    if len(patients) == 0:
        print("No patient records available.")
        return

    print("\n----- Patient List -----")

    for patient in patients:
        # printing out nicely formatted info
        print("\nPatient ID : " + str(patient["id"]))
        print("Name       : " + patient["name"])
        print("Age        : " + str(patient["age"]))
        print("Gender     : " + patient["gender"])
        print("Phone      : " + str(patient["phone"]))
        print("Address    : " + patient["address"])

def search_patient():
    patients = get_patients()
    val = input("Enter patient ID or name: ").lower()

    found_one = False
    for patient in patients:
        # checking both id and name loosely
        if patient["id"].lower() == val or val in patient["name"].lower():
            print("\nPatient found")
            print("ID      :", patient["id"])
            print("Name    :", patient["name"])
            print("Age     :", patient["age"])
            print("Gender  :", patient["gender"])
            print("Phone   :", patient["phone"])
            print("Address :", patient["address"])
            found_one = True
            break # just stopping at the first match for now

    if not found_one:
        print("Patient not found.")

def update_patient():
    patients = get_patients()
    pid = input("Enter patient ID: ")

    idx = -1
    for i in range(len(patients)):
        if patients[i]["id"] == pid:
            idx = i
            break

    if idx == -1:
        print("Patient not found.")
        return
        
    print("Leave blank if you don't want to change something.")

    name = input("Name: ")
    phone = input("Phone: ")
    address = input("Address: ")

    # update fields if provided
    if name != "":
        patients[idx]["name"] = name
    if phone != "":
        patients[idx]["phone"] = phone
    if address != "":
        patients[idx]["address"] = address

    save_patients(patients)
    print("Patient details updated.")

def delete_patient():
    patients = get_patients()
    pid = input("Enter patient ID to delete: ")

    # let's find and remove
    target = None
    for p in patients:
        if p["id"] == pid:
            target = p
            break

    if target:
        patients.remove(target)
        save_patients(patients)
        print("Patient record deleted.")
    else:
        print("Patient not found.")

def patient_menu():
    while True:
        print("\n===== PATIENT MANAGEMENT =====")
        print("1. Add patient")
        print("2. Show patients")
        print("3. Search patient")
        print("4. Update patient")
        print("5. Delete patient")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            show_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            break
        else:
            print("Invalid choice, pick between 1-6.")