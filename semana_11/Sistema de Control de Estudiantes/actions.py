from student import Student

def create_student(students_list):
    name = input("Inserte su nombre: ")
    score = input("Inserte su nota: ")
    students_list.append(Student(name, score))

def show_students(students_list):
    if not students_list:
        print("No students found.")
        return
    for s in students_list:
        print(f"Name: {s.name}, Score: {s.score_1}")
