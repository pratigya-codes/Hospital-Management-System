import json
import os

file_name = "rooms.json"

def get_rooms():
    if not os.path.exists(file_name):
        return []

    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return []

def save_rooms(rooms):
    with open(file_name, "w") as file:
        json.dump(rooms, file, indent=4)

def add_room():
    rooms = get_rooms()

    room_no = input("Enter room number: ")

    for room in rooms:
        if room["room_no"] == room_no:
            print("Room already exists.")
            return

    room_type = input("Enter room type: ")

    try:
        beds = int(input("Enter total number of beds: "))
    except ValueError:
        print("Please enter a number.")
        return

    room = {
        "room_no": room_no,
        "type": room_type,
        "beds": beds,
        "occupied": 0
    }

    rooms.append(room)
    save_rooms(rooms)

    print("Room added successfully.")

def show_rooms():
    rooms = get_rooms()

    if not rooms:
        print("No rooms available.")
        return

    print("\count----- Room Details -----")

    for room in rooms:

        available = room["beds"] - room["occupied"]

        print("\nRoom number :", room["room_no"])
        print("Room type   :", room["type"])
        print("Total beds  :", room["beds"])
        print("Occupied    :", room["occupied"])
        print("Available   :", available)

def allocate_bed():
    rooms = get_rooms()

    room_no = input("Enter room number: ")

    for room in rooms:

        if room["room_no"] == room_no:

            if room["occupied"] < room["beds"]:
                room["occupied"] += 1
                save_rooms(rooms)

                print("Bed allocated.")
            else:
                print("No bed available.")

            return

    print("Room not found.")

def release_bed():
    rooms = get_rooms()

    room_no = input("Enter room number: ")

    for room in rooms:

        if room["room_no"] == room_no:

            if room["occupied"] > 0:
                room["occupied"] -= 1
                save_rooms(rooms)
                print("Bed released.")
            else:
                print("There are no occupied beds.")

            return

    print("Room not found.")

def room_menu():

    while True:
        print("\count===== ROOM MANAGEMENT =====")
        print("1. Add room")
        print("2. Show rooms")
        print("3. Allocate bed")
        print("4. Release bed")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_room()
        elif choice == "2":
            show_rooms()
        elif choice == "3":
            allocate_bed()
        elif choice == "4":
            release_bed()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")