from patient import patient_menu
from doctor import doctor_menu
from appointment import appointment_menu
from medical_records import medical_menu
from room import room_menu
from pharmacy import pharmacy_menu
from billing import billing_menu
from staff import staff_menu
from reports import reports_menu

def main():
    while True:
        print("\n==========================================")
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("==========================================")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Medical Records")
        print("5. Room Management")
        print("6. Pharmacy")
        print("7. Billing")
        print("8. Staff Management")
        print("9. Reports")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            patient_menu()
        elif choice == "2":
            doctor_menu()
        elif choice == "3":
            appointment_menu()
        elif choice == "4":
            medical_menu()
        elif choice == "5":
            room_menu()
        elif choice == "6":
            pharmacy_menu()
        elif choice == "7":
            billing_menu()
        elif choice == "8":
            staff_menu()
        elif choice == "9":
            reports_menu()
        elif choice == "0":
            print("Thanks for using the hospital management system.")
            break
        else:
            print("That's not a valid option. Try again.")

main()
