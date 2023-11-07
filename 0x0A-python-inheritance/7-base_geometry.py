#!/usr/bin/python3

"""
This module contains the
base class of all the
geometries
"""


class BaseGeometry:
    """
    This is the base class
    of all geometries
    """

    def area(self):
        """
        This computes the
        area of the geometry
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the value
        before usage

        Args:
            name - name of value to insert
            value - the value
        """

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
