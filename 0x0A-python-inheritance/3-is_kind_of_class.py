#!/usr/bin/python3

"""
This module contains
a single function that
checks if an object
is instance of a class or
subclass of class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object
    is an instance othe class
    or class that inherits from
    class

    Args:
        obj - The object
        a_class - The class to check
    """

    return isinstance(obj, a_class)
