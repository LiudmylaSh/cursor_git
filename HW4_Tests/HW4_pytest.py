import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(0, 1) == 1
    assert Calculator.add(1, 10) == 11
    assert Calculator.add(0.3, 0.2) == 0.5
    assert Calculator.add("13", "13") == "1313"


def test_subtract():
    assert Calculator.subtract(4, 2) == 2
    assert Calculator.subtract(10, 0) == 10
    assert Calculator.subtract(7, -3) == 10
    assert Calculator.subtract(3.1, 0.1) == 3


def test_multiply():
    assert Calculator.multiply(0, 0) == 0
    assert Calculator.multiply(1, 1) == 1
    assert Calculator.multiply(-1, 2) == -2
    assert Calculator.multiply(-10, -10) == 100
    assert Calculator.multiply(-10, 10) == -100
    assert Calculator.multiply("1", 10) == "1111111111"
    assert Calculator.multiply(2, 0.1) == 0.2


def test_divide():
    assert Calculator.divide(0, 1) == 0
    assert Calculator.divide(10, 10) == 1
    assert Calculator.divide(100, -10) == -10
    assert Calculator.divide(100, 10) == 10
    assert Calculator.divide(9.9, 0.1) == 99
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)
