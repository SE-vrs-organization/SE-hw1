
# a "correct" function that would pass the test case
def calculate_square(number: int):
    return number**2

# a "wrong" function that would fail the test case (as is not calculating cube)
def calculate_cube(number: int):
    return number**4

def test_square():
    assert calculate_square(3) == 9

def test_cube():
    assert calculate_cube(3) == 27