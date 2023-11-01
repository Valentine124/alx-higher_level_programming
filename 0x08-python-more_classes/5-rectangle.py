#!/usr/bin/python3

"""
This module will contain
a rectangle class
"""


class Rectangle:
    """
    This class is used to
    construct the rectangle
    shape

    Attributes:
        - _Rectangle__width: The width of the rectangle shape
        - _Rectangle__height: The height of the rectangle shape
    """

    def __init__(self, width=0, height=0):
        """
        The class initializer

        Attributes:
            width - The width of the rectangle
            height - to set the height of the rectangle
        """

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self._Rectangle__height = height
        self._Rectangle__width = width

    @property
    def width(self):
        """
        getter method for the
        rectangle width
        """

        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        setter method for the rectangle
        width

        Attribute:
            value - value of the new width
        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self._Rectangle__width = value

    @property
    def height(self):
        """
        getter method for the
        rectangle height
        """

        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        setter method for the rectangle
        height

        Attribute:
            value - value of the new height
        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self._Rectangle__height = value

    def area(self):
        """
        This function computes the area
        of the rectangle
        """

        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        """
        This function computes the
        peimeter of the rectangle
        """

        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return 0
        else:
            return 2 * (self._Rectangle__height + self._Rectangle__width)

    def __str__(self):
        """
        Rectangle representation of the string
        """

        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return ""
        else:
            str = ""

            str2 = self._Rectangle__width * "#"

            str += str2

            for i in range(1, self._Rectangle__height):
                str += "\n"
                str2 = self._Rectangle__width * "#"
                str += str2

            return str

    def __repr__(self):
        """
        Return a string representation
        of the class object
        """

        return f'Rectangle({self._Rectangle__width},'\
            f' {self._Rectangle__height})'

    def __del__(self):
        print('Bye rectangle...')
