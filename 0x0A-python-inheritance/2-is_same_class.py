#!/usr/bin/python3

"""
This module contains a function
that checks if an object is an
instance of a class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of
    a class

    Args:
        obj - The object
        a_class - The class
    """

    return isinstance(obj, a_class)
