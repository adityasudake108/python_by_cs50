import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_string():
    with pytest.raises(TypeError):
        square("hello")



# def main():
#     test_square()

# def test_square():

#     # Method 1
#     # if square(2) !=4:
#     #     print("2 squared was not 4")
#     # if square(3) !=9:
#     #     print("3 squared was not 9")
#     # else:
#     #     print("All tests passed")


#     # Proper Method using "assert" key
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
        
    

# if __name__ == "__main__":
#     main()


# The assert statement is used to check if a condition is True. If the condition is False, the program will raise an AssertionError.
# If the condition is True, the program will continue to run.