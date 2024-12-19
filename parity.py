# x = int(input("What's X "))

# if x % 2 == 0:
#     print("Even:3", x)
# else:
#     print("Odd")

def main():
    x = int(input("What's X "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # if n % 2 == 0: Method 1
    #     return True
    # else:
    #     return False

    # return True if n % 2 == 0 else False  Method 2

    return n % 2 == 0 # Method 3: becoz it returns true or false itself



main()