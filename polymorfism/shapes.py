"""Shapes."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return math.pi * self.radius * self.radius


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.side * self.side


class Rectangle(Shape):
    """Retangle is a subclass of Shape."""

    def __init__(self, color: str, side_a: float, side_b: float):
        """Retangle constructor."""
        super().__init__(color)
        self.side_a = side_a
        self.side_b = side_b

    def __repr(self) -> str:
        """Return representation of the retangle."""
        return f"Retangle (l: {self.side_a}, w: {self.side_b}, color: {self.color}"

    def get_area(self) -> float:
        """
        Calculate the area of the retangle.

        Area of the square is side_a * side_b.
        """
        return self.side_a * self.side_b


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        shape_area_total = 0
        for shape in self.shapes:
            shape_area_total += shape.get_area()
        return shape_area_total

    def get_circles(self) -> list:
        """Return only circles."""
        all_circles = []
        for shape in self.shapes:
            if isinstance(shape, Circle):
                all_circles.append(shape)
        return all_circles

    def get_squares(self) -> list:
        """Return only squares."""
        all_squares = []
        for shape in self.shapes:
            if isinstance(shape, Square):
                all_squares.append(shape)
        return all_squares

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        all_rectangles = []
        for shape in self.shapes:
            if isinstance(shape, Rectangle):
                all_rectangles.append(shape)
        return all_rectangles


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_circles())
