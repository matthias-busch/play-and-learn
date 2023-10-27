import math
from typing import Any
from pytest_tutorial_freecodecamp.shapes import Circle, Rectangle

class TestCircle:

    def setup_method(self, method: Any) -> None:
        print(f"Setting up {method}")
        self.circle = Circle(10)

    def teardown_method(self, method: Any) -> None:
        print(f"Tear down {method}")

    def test_area(self) -> None:
        expected_value = math.pi * self.circle.radius ** 2
        assert self.circle.area() == expected_value

    def test_perimeter(self) -> None:
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle: Rectangle) -> None:
        assert self.circle.area() != my_rectangle.area()
