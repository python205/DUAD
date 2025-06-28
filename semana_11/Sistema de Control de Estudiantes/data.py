import csv
from student import Student

def export_to_csv(students, filename="estudiantes.csv"):
    if not students:
        print("No students to export.")
        return
    with open(filename, mode="w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=students[0].to_dict().keys())
        writer.writeheader()
        for student in students:
            writer.writerow(student.to_dict())
    print(f"Exported to {filename}")

def import_from_csv(filename="estudiantes.csv"):
    students = []
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(Student(row["name"], row["score_1"]))
    except FileNotFoundError:
        print("No CSV file found.")
    return students
