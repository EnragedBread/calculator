import pytest
import calculator as calc

def test_add_two_numbers():
    assert calc.calculate('Add', 1, 1) == 2

def test_add_two_floats():
    assert calc.calculate('Add', 2.5, 2.5) == 5.0

def test_throws_an_exception_for_invalid_method():
    with pytest.raises(calc.InvalidCalculateMethodError):
        calc.calculate('subtractiply', 25, 14)

def test_throws_an_exception_for_dividing_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.calculate('Divide', 10, 0)