#!/usr/bin/python3

"""
This module contains the
Rectangle objetct blueprint
that inherits from the
Base geometry class
"""


import sys
sys.path.append('..')
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
