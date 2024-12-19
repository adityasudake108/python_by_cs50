def main():
    ratio = int(input("Height: "))
    print_height(ratio)

def print_height(n):

    for i in range(n):
        # for j in range(n): # method 1
        #     print("#", end="")
        # print()
        print("#" * n) # method 2

main()