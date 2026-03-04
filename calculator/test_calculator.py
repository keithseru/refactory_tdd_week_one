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
    
# Test the multiplication function
def test_multiply():
    result = multiply(2,3)
    assert result == 6