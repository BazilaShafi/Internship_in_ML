def add_student(records, name, grades):
    records[name] = grades

def get_average(records, name):
    if name in records:
        return sum(records[name]) / len(records[name])
    else:
        return None

# Example usage
students = {}
add_student(students, "Bazila", [85, 90, 88])
add_student(students, "Naveed", [70, 75, 80])

for name in students:
    avg = get_average(students, name)
    print(f"{name}'s average: {avg}")
