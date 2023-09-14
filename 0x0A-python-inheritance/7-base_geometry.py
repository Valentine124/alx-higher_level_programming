#!/usr/bin/python3

"""
This module contains the base class
for geometries
"""


class BaseGeometry:
    """
    The base class for all geometries
    """

    def area(self):
        """
        This computes the area of the
        shape
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks if value is a an integer an
        not less than or equal to 0
        """

        if not (type(value) is int):
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
