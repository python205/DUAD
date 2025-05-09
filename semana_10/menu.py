from actions import *
from data import *

def show_menu():
    students = []
    while True:
        print("\nStudent Control System")
        print("1. Add student")
        print("2. View all")
        print("3. Show top 3 students")
        print("4. Show overall average")
        print("5. Export to CSV")
        print("6. Import from CSV")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_students(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            show_top3(students)
        elif choice == "4":
            show_average(students)
        elif choice == "5":
            export_to_csv(students)
        elif choice == "6":
            students = import_from_csv()
        elif choice == "0":
            break
        else:
            print("Invalid option. Try again.")
