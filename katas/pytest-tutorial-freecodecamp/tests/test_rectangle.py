from pytest_tutorial_freecodecamp.shapes import Rectangle


def test_area(my_rectangle: Rectangle) -> None:
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle: Rectangle) -> None:
    assert my_rectangle.perimeter() == 2 * (10 + 20)

def test_not_equal(my_rectangle: Rectangle, weird_rectangle: Rectangle) -> None:
    assert my_rectangle != weird_rectangle
