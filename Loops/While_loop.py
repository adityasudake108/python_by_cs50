# While loop: The while loop is used to execute a block of code as long as a certain condition is met

# while cat !=0:
#     print("Meow")
#     cat -= 1

# while True:
#     cat = int(input("How many times meow? "))
#     if cat > 0:
#         break

# for _ in range(cat):
#     print("Meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        cat = int(input("How many times meow? "))
        if cat > 0:
            return cat
        

def meow(n):
    for _ in range(n):
        print("meow")

main()