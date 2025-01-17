# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
        


#Code 2

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

#Above code reads student names and houses from students.csv, formats them into strings, sorts the list of formatted strings, and prints each sorted entry.

#Code 3

students = []
with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

# def get_name(student):
#     return student["name"] # we use key word lamda to make the code more concise

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")  

# This code reads student names and houses from students.csv, stores them in a list of dictionaries,
# sorts the list by student names, and prints each student's name and house.