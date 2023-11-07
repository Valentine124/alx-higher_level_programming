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
