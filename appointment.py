import json
import os

file_name = "appointments.json"

def get_appointments():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return []

def save_appointments(appointments):
    with open(file_name, "w") as file:
        json.dump(appointments, file, indent=4)

def book_appointment():
    appointments = get_appointments()
    aid = input("Enter appointment ID: ")

    for appointment in appointments:
        if appointment["id"] == aid:
            print("Appointment ID already exists.")
            return

    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    date = input("Enter date: ")
    time = input("Enter time: ")

    new_appointment = {
        "id": aid,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time,
        "status": "Booked"
    }

    appointments.append(new_appointment)
    save_appointments(appointments)
    print("Appointment booked successfully.")

def show_appointments():
    appointments = get_appointments()
    if not appointments:
        print("No appointments available.")
        return

    print("\n----- Appointments -----")
    for appointment in appointments:
        print("\nAppointment ID :", appointment["id"])
        print("Patient ID     :", appointment["patient_id"])
        print("Doctor ID      :", appointment["doctor_id"])
        print("Date           :", appointment["date"])
        print("Time           :", appointment["time"])
        print("Status         :", appointment["status"])

def cancel_appointment():
    appointments = get_appointments()
    aid = input("Enter appointment ID: ")

    for appointment in appointments:
        if appointment["id"] == aid:
            if appointment["status"] == "Cancelled":
                print("Appointment is already cancelled.")
                return

            appointment["status"] = "Cancelled"
            save_appointments(appointments)
            print("Appointment cancelled.")
            return

    print("Appointment not found.")

def patient_appointments():
    appointments = get_appointments()
    pid = input("Enter patient ID: ")
    found = False

    for appointment in appointments:
        if appointment["patient_id"] == pid:
            print("\nAppointment ID :", appointment["id"])
            print("Doctor ID      :", appointment["doctor_id"])
            print("Date           :", appointment["date"])
            print("Time           :", appointment["time"])
            print("Status         :", appointment["status"])
            found = True

    if not found:
        print("No appointments found for this patient.")

def appointment_menu():
    while True:
        print("\n===== APPOINTMENT MANAGEMENT =====")
        print("1. Book appointment")
        print("2. Show appointments")
        print("3. Patient appointments")
        print("4. Cancel appointment")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_appointment()
        elif choice == "2":
            show_appointments()
        elif choice == "3":
            patient_appointments()
        elif choice == "4":
            cancel_appointment()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")