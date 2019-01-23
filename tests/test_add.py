"""
Calculator to add
"""
from calculator import add

def test_two_plus_two():
    """
    Given 2 and 2 as parameters, 4 returned
    """
    assert add(2, 2) == 4

def test_no_parameters():
    """
    If no parameters provided, return o.
    """
    assert add() == 0

def test_one_two_three():
    assert add(1, 2, 3) == 6
