import math
from abc import ABC, abstractmethod
from typing import Any


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimeter(self) -> float:
        ...


class Circle(Shape):

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return (self.area() == other.area() and self.perimeter() == other.perimeter())


    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> int | float:
        return 2 * (self.length + self.width)


class Square(Rectangle):

    def __init__(self, side_length: int) -> None:
        super().__init__(side_length, side_length)
