from actions import create_student, show_students
from data import export_to_csv, import_from_csv

def show_menu():
    students = []
    while True:
        print("\nStudent Control System")
        print("1. Add student")
        print("2. View all students")
        print("5. Export to CSV")
        print("6. Import from CSV")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "5":
            export_to_csv(students)
        elif choice == "6":
            students = import_from_csv()
        elif choice == "0":
            break
        else:
            print("Invalid option. Try again.")
