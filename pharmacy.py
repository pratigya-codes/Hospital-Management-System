import json
import os

file_name = "medicines.json"

def get_medicines():
    if not os.path.exists(file_name):
        return []

    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except Exception:
        return []

def save_medicines(medicines):
    with open(file_name, "w") as file:
        json.dump(medicines, file, indent=4)

def add_medicine():
    medicines = get_medicines()
    mid = input("Enter medicine ID: ")

    for medicine in medicines:
        if medicine["id"] == mid:
            print("Medicine already exists.")
            return

    name = input("Enter medicine name: ")

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    except ValueError:
        print("Enter valid numbers.")
        return

    expiry = input("Enter expiry date: ")

    medicine = {
        "id": mid,
        "name": name,
        "quantity": quantity,
        "price": price,
        "expiry": expiry
    }

    medicines.append(medicine)
    save_medicines(medicines)
    print("Medicine added successfully.")

def show_medicines():
    medicines = get_medicines()
    if not medicines:
        print("No medicines available.")
        return

    print("\n----- Pharmacy Stock -----")
    for medicine in medicines:
        print("\nMedicine ID :", medicine["id"])
        print("Name        :", medicine["name"])
        print("Quantity    :", medicine["quantity"])
        print("Price       :", medicine["price"])
        print("Expiry      :", medicine["expiry"])

def search_medicine():
    medicines = get_medicines()
    value = input("Enter medicine ID or name: ").lower()

    for medicine in medicines:
        if medicine["id"].lower() == value or value in medicine["name"].lower():
            print("\nMedicine found")
            print("ID       :", medicine["id"])
            print("Name     :", medicine["name"])
            print("Quantity :", medicine["quantity"])
            print("Price    :", medicine["price"])
            print("Expiry   :", medicine["expiry"])
            return

    print("Medicine not found.")

def sell_medicine():
    medicines = get_medicines()
    mid = input("Enter medicine ID: ")

    for medicine in medicines:
        if medicine["id"] == mid:
            try:
                amount = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity.")
                return

            if amount > medicine["quantity"]:
                print("Not enough stock.")
                return

            if amount <= 0:
                print("Invalid quantity.")
                return

            total = amount * medicine["price"]
            medicine["quantity"] -= amount
            save_medicines(medicines)
            print("Medicine sold.")
            print("Total amount =", total)
            return

    print("Medicine not found.")

def pharmacy_menu():
    while True:
        print("\n===== PHARMACY =====")
        print("1. Add medicine")
        print("2. Show medicines")
        print("3. Search medicine")
        print("4. Sell medicine")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_medicine()
        elif choice == "2":
            show_medicines()
        elif choice == "3":
            search_medicine()
        elif choice == "4":
            sell_medicine()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")