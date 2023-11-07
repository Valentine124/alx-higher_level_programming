#!/usr/bin/python3

"""
This module contains
theRectangle objetct blueprint
that inherits from the
Basegeometry class
and it is used to draw
the rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class will be used
    to draw the rectangle
    shape

    Attributes:
        _Rectangle__width - the width of the rectangle
        _Rectangle__height - the height of the rectangle
    """

    def __init__(self, width, height):
        """
        object initializer

        Args:
            width - for the width
            height - for the height
        """

        super().integer_validator('width', width)
        super().integer_validator('height', height)

        self._Rectangle__width = width
        self._Rectangle__height = height

    def __str__(self):
        return f'[Rectangle] {self._Rectangle__width}/'\
                '{self._Rectangle__height}'

    def area(self):
        """
        Area implementation
        of the Rectangle class
        """

        return self._Rectangle__width * self._Rectangle__height
