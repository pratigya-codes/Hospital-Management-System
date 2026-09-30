# 🏥 Hospital Management System

A Python-based **Hospital Management System** designed to manage patient
records, doctor details, appointments, medical records, rooms, pharmacy,
billing, staff, and basic hospital reports.

------------------------------------------------------------------------

## 📌 About the Project

The Hospital Management System is a **console-based Python application**
developed to demonstrate the practical use of Python programming
concepts through a real-world management system.

The project is divided into multiple modules, with each module
responsible for a specific hospital operation. The system uses **JSON
files for local data storage** and does not require an external database
or internet connection.

------------------------------------------------------------------------

## 🎯 Objectives

-   Manage patient records efficiently.
-   Manage doctor information.
-   Book and manage appointments.
-   Maintain patient medical records.
-   Manage hospital rooms and beds.
-   Maintain pharmacy and medicine stock.
-   Generate and manage patient bills.
-   Manage hospital staff and attendance.
-   Generate basic hospital reports.
-   Demonstrate Python concepts such as functions, loops, conditional
    statements, modules, lists, dictionaries, file handling, and JSON.

------------------------------------------------------------------------

## ⚙️ Features

### 👨‍⚕️ Patient Management

-   Add new patients
-   View all patients
-   Search patients
-   Update patient information
-   Delete patient records

### 🩺 Doctor Management

-   Add doctors
-   View doctors
-   Search doctors
-   Update doctor information
-   Delete doctor records

### 📅 Appointment Management

-   Book appointments
-   View appointments
-   Search patient appointments
-   Cancel appointments

### 📋 Medical Records

-   Add medical records
-   View medical records
-   View patient medical history

### 🏨 Room Management

-   Add hospital rooms
-   View room details
-   Allocate beds
-   Release beds
-   Check available beds

### 💊 Pharmacy Management

-   Add medicines
-   View medicine stock
-   Search medicines
-   Sell medicines
-   Track available quantity

### 💰 Billing Management

-   Create patient bills
-   View bills
-   Pay bills
-   Search patient bills
-   Track paid and unpaid bills

### 👩‍💼 Staff Management

-   Add staff members
-   View staff
-   Search staff
-   Mark attendance

### 📊 Reports

-   Generate hospital summary reports
-   View low-stock medicines
-   View unpaid bills
-   View hospital statistics

------------------------------------------------------------------------

## 📁 Project Structure

``` text
Hospital-Management-System/
│
├── main.py
├── patient.py
├── doctor.py
├── appointment.py
├── medical_records.py
├── room.py
├── pharmacy.py
├── billing.py
├── staff.py
├── reports.py
│
├── patients.json
├── doctors.json
├── appointments.json
├── medical_records.json
├── rooms.json
├── medicines.json
├── bills.json
├── staff.json
│
├── README.md
└── .gitignore
```

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Python 3**
-   JSON
-   File Handling
-   Functions
-   Conditional Statements
-   Loops
-   Lists
-   Dictionaries
-   Modules
-   Exception Handling

------------------------------------------------------------------------

## 💻 Requirements

-   Python 3.x installed
-   A computer or laptop
-   Terminal or Command Prompt
-   VS Code or any Python-compatible IDE

The project primarily uses Python's built-in libraries and does not
require external packages.

------------------------------------------------------------------------

## ▶️ How to Run

### 1. Clone the repository

``` bash
git clone https://github.com/pratigya-codes/Hospital-Management-System.git
```

### 2. Open the project folder

``` bash
cd Hospital-Management-System
```

### 3. Run the main program

``` bash
python main.py
```

------------------------------------------------------------------------

## 🖥️ Main Menu

When the program starts, the following menu is displayed:

``` text
==========================================
       HOSPITAL MANAGEMENT SYSTEM
==========================================

1. Patient Management
2. Doctor Management
3. Appointment Management
4. Medical Records
5. Room Management
6. Pharmacy
7. Billing
8. Staff Management
9. Reports
0. Exit

Enter your choice:
```

The user can select an option to access the corresponding module.

------------------------------------------------------------------------

## 🗂️ Data Storage

The system stores its information locally using JSON files.

  File                     Purpose
  ------------------------ ----------------------------------
  `patients.json`          Patient information
  `doctors.json`           Doctor information
  `appointments.json`      Appointment records
  `medical_records.json`   Patient medical records
  `rooms.json`             Room and bed information
  `medicines.json`         Pharmacy inventory
  `bills.json`             Patient billing information
  `staff.json`             Staff information and attendance

This allows the data to remain available even after the program is
closed.

------------------------------------------------------------------------

## 🔄 Working of the System

The basic working flow of the application is:

``` text
User
  ↓
main.py
  ↓
Select an Operation
  ↓
Required Python Module
  ↓
Read JSON Data
  ↓
Validate Input
  ↓
Perform Operation
  ↓
Update Records
  ↓
Save Data
  ↓
Display Result
```

------------------------------------------------------------------------

## 🧪 Sample Operations

The project demonstrates several operations, such as:

-   Registering a new patient
-   Adding a doctor
-   Booking an appointment
-   Creating a medical record
-   Allocating a hospital bed
-   Selling medicine
-   Generating a patient bill
-   Marking staff attendance
-   Generating hospital reports

------------------------------------------------------------------------

## 📚 Python Concepts Demonstrated

-   Variables and data types
-   `if`, `elif`, and `else`
-   `for` loops
-   `while` loops
-   Functions
-   Lists
-   Dictionaries
-   Modules and imports
-   File handling
-   JSON handling
-   Exception handling
-   Input validation

------------------------------------------------------------------------

## ⚠️ Limitations

This project is designed primarily for educational purposes.

-   It uses JSON files instead of a database.
-   It is a console-based application.
-   It does not have a graphical user interface.
-   It does not contain an authentication or login system.
-   It does not provide online hospital services.
-   It is not intended for use in an actual hospital environment.

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   Database integration using MySQL or SQLite
-   Graphical user interface
-   Web-based interface
-   Login and authentication
-   Role-based access for doctors, staff, and administrators
-   Advanced reports and dashboards
-   Improved invoice and payment system
-   Advanced patient search
-   Backup and restore functionality

------------------------------------------------------------------------

## 🎓 Purpose

This project was developed as a **Python programming project** to
demonstrate the practical implementation of programming concepts through
a real-world Hospital Management System.

It provides hands-on experience with modular programming, file handling,
JSON data storage, functions, loops, conditional statements, and record
management.

------------------------------------------------------------------------

## 👨‍💻 Author

**Pratigya Gupta**

GitHub: [@pratigya-codes](https://github.com/pratigya-codes)

------------------------------------------------------------------------

## 📄 License

This project is created for educational purposes.
