import pytest
from calculator import add, subtract, divide, multiply

# Test 1: Testing the addition function
def test_add():
    result = add(2,3)
    assert result == 5

# Test 2: Testing the subtraction function
def test_subtract():
    result = subtract(2,3)
    assert result == -1
    
# Test 3: Test the multiplication function
def test_multiply():
    result = multiply(2,3)
    assert result == 6

# Test 4: Test the division function
def test_divide():
    result = divide(4,2)
    assert result == 2
    
# Test 5: Raising an error when diving by zero
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)