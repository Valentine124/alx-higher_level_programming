#!/usr/bin/python3

"""
This module implements the typr for
Rectangle that inherits from the
BaseGeometry class
"""


class Rectangle(BaseGeometry):
    """
    This class create the Rectangle
    inheriting from the BaseGeometry

    Attributes:
        _Rectangle__width - The rectangle width
        _Rectangle__height - The rectangle height
    """

    def __init__(self, width, height):
        """
        Rectangle initializer

        Args:
            width - The width
            height - The height
        """

        self._Rectangle__width = width
        self._Rectangle__height = height

        super().integer_validator("Rectangle", self._Rectangle__width)
        super().integer_validator("Rectangle", self._Rectangle__height)
