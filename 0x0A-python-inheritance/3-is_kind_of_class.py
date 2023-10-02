#!/usr/bin/python3

"""
This module contains a single function
"""


def is_kind_of_class(obj, a_class):
    """
    Tells if an object is an instance
    of a class or a derive class

    Args:
        obj - The object
        a_class - The class
    """

    return isinstance(obj, a_class)
