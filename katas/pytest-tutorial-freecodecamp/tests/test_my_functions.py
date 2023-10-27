import pytest
import time
from pytest_tutorial_freecodecamp.my_functions import add, divide

def test_add() -> None:
    result = add(number_one=1, number_two=4)

    assert result == 5


def test_add_strings() -> None:
    result = add(number_one="i like ", number_two="burgers") # type: ignore
    assert result == "i like burgers" # type: ignore

def test_divide() -> None:
    result = divide(number_one=4, number_two=2)

    assert result == 2

def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(number_one=10, number_two=0)

@pytest.mark.slow
def test_very_slow() -> None:
    time.sleep(2)
    result = divide(number_one=4, number_two=2)

    assert result == 2

@pytest.mark.skip(reason="This feature is currently broken")
def test_add_skip() -> None:
    assert add(1, 2) == 3

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken() -> None:
    divide(3, 0)
