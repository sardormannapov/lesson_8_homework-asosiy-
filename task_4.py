get_students = {
    "Student 1": "Steve",
    "Student 2": "Becky",
    "Student 3": "John"
}
result = []

for value in get_students.values():
    result.append(value)
    sortirovka = sorted(result)
print(sortirovka)
