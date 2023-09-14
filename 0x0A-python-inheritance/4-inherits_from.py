#!/usr/bin/python3

"""
This module contains a single function
"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of
    a class that inherits from a class

    Args:
        obj - The object
        a_class - The class
    """

    return issubclass(type(obj), a_class)
