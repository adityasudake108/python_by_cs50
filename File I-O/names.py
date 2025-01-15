# name = input("What is your name? ")


# Open file in write mode

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# Using "with" statement to open file in write mode and close it automatically

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# Open file in read mode

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.strip())

names = []

with open("names.txt") as file:
    for line in sorted(file): # by using "reverse=True" in sorted() function, we can sort the names in descending order
        print(line.rstrip())

