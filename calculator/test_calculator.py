import pytest
from calculator import add, subtract, divide, multiply

# Test 1: Testing the addition function
def test_add():
    result = add(2,3)
    assert result == 5