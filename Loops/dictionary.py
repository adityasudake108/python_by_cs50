# dictionary: dictionary is mutable dictionary is unordered collection of key-value pairs key is immutable, value can be mutable or immutable

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student ], sep=", ")