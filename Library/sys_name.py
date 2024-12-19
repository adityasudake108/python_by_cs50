import sys
    # print("Hello, my name is", sys.argv[1])

# try:
#     print("Hello, my name is", sys.argv[1])   ### Method 1
# except IndexError:
#     print("Please provide a name")

if len(sys.argv) < 2:                           ### Method 2
    sys.exit("Please provide a name")
elif len(sys.argv) > 2:
    sys.exit("You provided too many names")
else:
    print("Hello, my name is", sys.argv[1])


# if you want to print the name of the script, you can use sys.argv[0] as well.
# you want to print the name like David John, you should insert between " ".

# sys.exit("Please provide a name")   This will exit the program and print the message.


