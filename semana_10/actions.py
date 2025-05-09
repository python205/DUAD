def add_students(students):
    n = int(input("How many students to add? "))
    for _ in range(n):
        student = {}
        student["name"] = input("Name: ")
        student["section"] = input("Section: ")
        for subject in ["espanol", "ingles", "sociales", "ciencias"]:
            while True:
                try:
                    grade = int(input(f"{subject.capitalize()} grade (0-100): "))
                    if 0 <= grade <= 100:
                        student[subject] = grade
                        break
                    else:
                        print("Grade must be 0-100.")
                except ValueError:
                    print("Enter a valid number.")
        students.append(student)

def show_students(students):
    for s in students:
        print(s)

def show_top3(students):
    sorted_list = sorted(students, key=lambda s: average(s), reverse=True)
    for s in sorted_list[:3]:
        print(s["name"], "Avg:", average(s))

def show_average(students):
    if students:
        total = sum(average(s) for s in students)
        print("Class average:", total / len(students))
    else:
        print("No students.")

def average(s):
    return (s["espanol"] + s["ingles"] + s["sociales"] + s["ciencias"]) / 4
