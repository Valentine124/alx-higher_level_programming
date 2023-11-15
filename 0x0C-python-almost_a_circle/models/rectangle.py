#!/usr/bin/python3

"""
rectangle module which
contains the Rectangle
class
"""


from models.base import Base


class Rectangle(Base):
    """
    This class is the
    implementation of Rectangle

    Attributes:
        __width - the rectangle width
        __height - the rectangle height
        __x - the x coordinate
        __y - the y coordinate
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        width(width)
        height(height)
        x(x)
        y(y)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
