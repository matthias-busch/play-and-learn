import pytest

from pytest_tutorial_freecodecamp.shapes import Rectangle

@pytest.fixture
def my_rectangle() -> Rectangle:
    return Rectangle(length=10, width=20)

@pytest.fixture
def weird_rectangle() -> Rectangle:
    return Rectangle(length=5, width=6)
