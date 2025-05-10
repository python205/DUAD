import csv

def export_to_csv(students, filename="estudiantes.csv"):
    with open(filename, mode="w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)
    print("Exported to estudiantes.csv")

def import_from_csv(filename="estudiantes.csv"):
    try:
        with open(filename, newline='') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print("No CSV file found.")
        return []
