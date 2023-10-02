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
