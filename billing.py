import json
import os

file_name = "bills.json"

def get_bills():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except Exception:
        return []

def save_bills(bills):
    with open(file_name, "w") as file:
        json.dump(bills, file, indent=4)

def create_bill():
    bills = get_bills()

    bid = input("Enter bill ID: ")
    patient_id = input("Enter patient ID: ")

    try:
        doctor_fee = float(input("Doctor/consultation fee: "))
        room_charge = float(input("Room charge: "))
        medicine_charge = float(input("Medicine charge: "))
        other_charge = float(input("Other charges: "))
    except ValueError:
        print("Please enter valid amounts.")
        return

    total = doctor_fee + room_charge + medicine_charge + other_charge

    bill = {
        "id": bid,
        "patient_id": patient_id,
        "doctor_fee": doctor_fee,
        "room_charge": room_charge,
        "medicine_charge": medicine_charge,
        "other_charge": other_charge,
        "total": total,
        "status": "Unpaid"
    }

    bills.append(bill)
    save_bills(bills)

    print("\n----- BILL -----")
    print("Bill ID         :", bid)
    print("Patient ID      :", patient_id)
    print("Doctor fee      :", doctor_fee)
    print("Room charge     :", room_charge)
    print("Medicine charge :", medicine_charge)
    print("Other charges   :", other_charge)
    print("-------------------------")
    print("Total           :", total)

def show_bills():
    bills = get_bills()

    if not bills:
        print("No bills available.")
        return

    print("\n----- Bills -----")
    for bill in bills:
        print("\nBill ID    :", bill["id"])
        print("Patient ID :", bill["patient_id"])
        print("Total      :", bill["total"])
        print("Status     :", bill["status"])

def pay_bill():
    bills = get_bills()
    bid = input("Enter bill ID: ")
    for bill in bills:
        if bill["id"] == bid:
            if bill["status"] == "Paid":
                print("Bill is already paid.")
                return
            bill["status"] = "Paid"
            save_bills(bills)
            print("Bill payment completed.")
            return
    print("Bill not found.")

def find_patient_bill():
    bills = get_bills()
    pid = input("Enter patient ID: ")
    found = False
    for bill in bills:
        if bill["patient_id"] == pid:
            print("\nBill ID :", bill["id"])
            print("Amount  :", bill["total"])
            print("Status  :", bill["status"])
            found = True
    if not found:
        print("No bills found.")

def billing_menu():
    while True:
        print("\n===== BILLING =====")
        print("1. Create bill")
        print("2. Show bills")
        print("3. Pay bill")
        print("4. Find patient bill")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_bill()
        elif choice == "2":
            show_bills()
        elif choice == "3":
            pay_bill()
        elif choice == "4":
            find_patient_bill()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
            