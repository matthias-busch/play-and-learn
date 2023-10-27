import pytest

from pytest_tutorial_freecodecamp.shapes import Square

@pytest.mark.parametrize(
    argnames=[
        "side_length",
        "expected_area"
    ],
    argvalues=[
        (5, 25),
        (4, 16),
        (9, 81)
    ],
    ids=[
        "side_length_5",
        "side_length_4",
        "side_length_9",
    ]
)
def test_multiple_square_areas(side_length: int, expected_area: float | int) -> None:
    assert Square(side_length).area() == expected_area


@pytest.mark.parametrize(
    argnames=[
        "side_length",
        "expected_perimeter"
    ],
    argvalues=[
        (3, 12),
        (4, 16),
        (5, 20)
    ]
)
def test_multiple_perimeters(side_length: int, expected_perimeter: float | int) -> None:
    assert Square(side_length).perimeter() == expected_perimeter
