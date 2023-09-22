#!/usr/bin/python3

"""
This module contains a class
thet defines a rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    This class inherits from
    the base class and contains
    all attributes needed by a
    rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The class initilizer
        """

        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        elif type(y) is not int:
            raise TypeError("y must be an integer")
        else:
            if width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width

            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height

            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height >= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(height) is not int:
            raise TypeError("y must be an integer")
        if height < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        This function calculates the
        area of the rectangle and
        returns it
        """

        return self.__height * self.__width

    def display(self):
        """
        This function displys 
        the rectangle instance
        as #
        """

        for first in range(0, self.__height):
            for sec in range(0, self.__width):
                if sec == (self.__width - 1):
                    print("#")
                else:
                    print("#", end="")
