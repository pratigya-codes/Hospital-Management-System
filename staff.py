import json
import os

file_name = "staff.json"

def get_staff():
    if not os.path.exists(file_name):
        return []

    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return []

def save_staff(staff):
    with open(file_name, "w") as file:
        json.dump(staff, file, indent=4)

def add_staff():
    staff = get_staff()

    sid = input("Enter staff ID: ")

    for person in staff:
        if person["id"] == sid:
            print("Staff ID already exists.")
            return

    name = input("Enter staff name: ")
    role = input("Enter role: ")
    department = input("Enter department: ")
    phone = input("Enter phone number: ")

    person = {
        "id": sid,
        "name": name,
        "role": role,
        "department": department,
        "phone": phone,
        "attendance": 0
    }

    staff.append(person)
    save_staff(staff)

    print("Staff member added.")

def show_staff():
    staff = get_staff()

    if not staff:
        print("No staff records found.")
        return

    print("----- Staff Details -----")

    for person in staff:
        print()
        print("ID         :", person["id"])
        print("Name       :", person["name"])
        print("Role       :", person["role"])
        print("Department :", person["department"])
        print("Phone      :", person["phone"])
        print("Attendance :", person["attendance"])

def search_staff():
    staff = get_staff()
    value = input("Enter staff ID or name: ").lower()

    for person in staff:
        if person["id"].lower() == value or value in person["name"].lower():
            print("\nStaff found")
            print("ID         :", person["id"])
            print("Name       :", person["name"])
            print("Role       :", person["role"])
            print("Department :", person["department"])
            print("Phone      :", person["phone"])
            print("Attendance :", person["attendance"])
            return

    print("Staff member not found.")

def mark_attendance():
    staff = get_staff()
    sid = input("Enter staff ID: ")

    for person in staff:
        if person["id"] == sid:
            person["attendance"] += 1
            save_staff(staff)
            print("Attendance marked.")
            return

    print("Staff member not found.")

def staff_menu():
    while True:
        print("===== STAFF MANAGEMENT =====")
        print("1. Add staff")
        print("2. Show staff")
        print("3. Search staff")
        print("4. Mark attendance")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_staff()
        elif choice == "2":
            show_staff()
        elif choice == "3":
            search_staff()
        elif choice == "4":
            mark_attendance()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
            