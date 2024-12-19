while True:
    try:
        x = int(input("What's x?"))
        # print("X is", x)
    except ValueError:
        print("X is not an integer.")
    else:
        break

print("X is", x)


# there are two ways to handle exceptions in Python:
# 1. Using try and except blocks
# 2. Using the else block
# The else block is used to handle the case when the code in the try block runs successfully. In
# this case, we are using the else block to break out of the loop when the input is successfully
# converted to an integer. If the input is not an integer, the except block will run and the loop will
# continue. If the input is successfully converted to an integer, the else block will run and the loop
# will break. 

"""There are different types of error occurs in Python:
1. SyntaxError: This error occurs when Python encounters a syntax error in the code.
2. IndentationError: This error occurs when the code is not properly indented.
3. NameError: This error occurs when a variable is not defined.
4. TypeError: This error occurs when an operation is performed on an object of an inappropriate type.
5. ValueError: This error occurs when a function receives an argument of the correct type but an inappropriate value.
"""

