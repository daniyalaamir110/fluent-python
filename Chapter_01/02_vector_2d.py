"""
A 2D vector class: Vector2

This module contains the implementation of a 2D vector class.

It is an example of a user-defined class that implements special methods
for operators like `+`, `*`, and other operations like `abs`, `bool`, `dot`,
and `cross`.
"""

import math


class Vector2:
    """A 2D vector class."""

    def __init__(self, x=0, y=0):
        """Initialize the 2D vector.

        Args:
            `x` (`float`): The x-coordinate of the vector.
            `y` (`float`): The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __abs__(self):
        # return math.sqrt(self.x ** 2 + self.y ** 2)
        return math.hypot(self.x, self.y)  # identical to the above

    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def dot(self, other):
        """Dot product of two vectors.

        The dot product of two vectors is the sum of the products of the
        corresponding components.

        Args:
            `other` (`Vector2`): The other vector.
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """Cross product of two vectors.

        The cross product of two vectors is the determinant of the matrix
        formed by the two vectors.

        Args:
            `other` (`Vector2`): The other vector.
        """

        return self.x * other.y - self.y * other.x
