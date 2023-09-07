#!/usr/bin/python3
"""
The module contains a class that
have some attributes
"""


class Rectangle:
    """
    The class defines a Rectangle with
    a width and a height

    Attributes:
        _width - private width
        _height - private height
    """


    def __init__(self, width=0, height=0):
        """
        The class initializer

        Args:
            width - The rectangle width
            height - The rectangle height
        """

        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        """
        The getter function for
        the width attribute
        """

        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        The width seeter function
        """

        if not (type(value) is int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__width = value

    @property
    def height(self):
        """
        The getter function for 
        the height attribute
        """

        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        The setter func for the height
        attribute

        Args:
            value - The value for the height
        """

        if not (type(value) is int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle__height = value
