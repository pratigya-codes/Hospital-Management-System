import json
import os

def read_file(file_name):
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return []

def hospital_report():
    patients = read_file("patients.json")
    doctors = read_file("doctors.json")
    appointments = read_file("appointments.json")
    rooms = read_file("rooms.json")
    medicines = read_file("medicines.json")
    bills = read_file("bills.json")
    staff = read_file("staff.json")

    print("\n========== HOSPITAL REPORT ==========")

    print("Number of patients     :", len(patients))
    print("Number of doctors      :", len(doctors))
    print("Appointments           :", len(appointments))
    print("Rooms                  :", len(rooms))
    print("Different medicines    :", len(medicines))
    print("Bills generated        :", len(bills))
    print("Staff members          :", len(staff))

    total_beds = 0
    occupied = 0

    for room in rooms:
        total_beds += room.get("beds", 0)
        occupied += room.get("occupied", 0)

    print("\nTotal beds             :", total_beds)
    print("Occupied beds          :", occupied)
    print("Available beds         :", total_beds - occupied)

    total_money = 0
    for bill in bills:
        if bill.get("status") == "Paid":
            total_money += bill.get("total", 0)

    print("Total money received   :", total_money)

def low_stock():
    medicines = read_file("medicines.json")
    print("\n===== LOW STOCK MEDICINES =====")
    found = False
    for medicine in medicines:
        if medicine.get("quantity", 0) <= 10:
            print(medicine.get("name", "Unknown"), "-", medicine.get("quantity", 0), "left")
            found = True
    if not found:
        print("No medicine is low in stock.")

def unpaid_bills():
    bills = read_file("bills.json")
    print("\n===== UNPAID BILLS =====")
    found = False
    for bill in bills:
        if bill.get("status") == "Unpaid":
            print("Bill ID:", bill.get("id", "Unknown"), "| Patient:", bill.get("patient_id", "Unknown"), "| Amount:", bill.get("total", 0))
            found = True
    if not found:
        print("There are no unpaid bills.")

def reports_menu():
    while True:
        print("\n===== REPORTS =====")
        print("1. Hospital report")
        print("2. Low stock medicines")
        print("3. Unpaid bills")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            hospital_report()
        elif choice == "2":
            low_stock()
        elif choice == "3":
            unpaid_bills()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
