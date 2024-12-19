# Ask user for their name
# name = input("What's your name? ")

# Remove whitespace from string and capitalize user's name
# name = name.strip().title()

# print(f"hello, {name}")

# Define using def key word

def hello(to = "World!"):
    print("Hello,", to)
hello()
name = input("What's your name? ")
hello(name)
