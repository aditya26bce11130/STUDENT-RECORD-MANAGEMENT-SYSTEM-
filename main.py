import json

FILE = "hostel_records.json"
def load_records():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_records(records):
    with open(FILE, "w") as file:
        json.dump(records, file, indent=4)
def add_student(records):
    print("\n--- Add Student ---")

    student = {
        "roll_no": input("Enter Roll Number: "),
        "name": input("Enter Student Name: "),
        "room_no": input("Enter Room Number: "),
        "branch": input("Enter Branch: "),
        "phone": input("Enter Phone Number: ")
    }

    records.append(student)
    save_records(records)

    print("Student record added successfully!")
def view_students(records):
    print("\n--- Hostel Records ---")

    if len(records) == 0:
        print("No records found.")
        return

    for student in records:
        print("\nRoll No :", student["roll_no"])
        print("Name    :", student["name"])
        print("Room No :", student["room_no"])
        print("Branch  :", student["branch"])
        print("Phone   :", student["phone"])
def search_student(records):
    print("\n--- Search Student ---")

    roll_no = input("Enter Roll Number: ")

    for student in records:
        if student["roll_no"] == roll_no:
            print("\nRecord Found!")
            print("Name   :", student["name"])
            print("Room   :", student["room_no"])
            print("Branch :", student["branch"])
            print("Phone  :", student["phone"])
            return

    print("Student record not found.")
def update_student(records):
    print("\n--- Update Student ---")

    roll_no = input("Enter Roll Number: ")

    for student in records:
        if student["roll_no"] == roll_no:

            student["name"] = input("Enter New Name: ")
            student["room_no"] = input("Enter New Room Number: ")
            student["branch"] = input("Enter New Branch: ")
            student["phone"] = input("Enter New Phone Number: ")

            save_records(records)

            print("Record updated successfully!")
            return

    print("Student record not found.")
def delete_student(records):
    print("\n--- Delete Student ---")

    roll_no = input("Enter Roll Number: ")

    for student in records:
        if student["roll_no"] == roll_no:
            records.remove(student)
            save_records(records)

            print("Record deleted successfully!")
            return

    print("Student record not found.")
def main():
    records = load_records()

    while True:
        print("\n==============================")
        print(" HOSTEL RECORD MANAGEMENT")
        print("==============================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(records)

        elif choice == "2":
            view_students(records)

        elif choice == "3":
            search_student(records)

        elif choice == "4":
            update_student(records)

        elif choice == "5":
            delete_student(records)

        elif choice == "6":
            print("Thank you for using Hostel Record Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
