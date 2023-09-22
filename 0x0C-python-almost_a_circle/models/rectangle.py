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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
