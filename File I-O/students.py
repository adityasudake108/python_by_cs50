# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
        


#code 2

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

#Above code reads student names and houses from students.csv, formats them into strings, sorts the list of formatted strings, and prints each sorted entry.