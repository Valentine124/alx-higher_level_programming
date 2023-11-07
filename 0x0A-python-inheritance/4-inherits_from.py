#!/usr/bin/python3

"""
This module contains
a single function that
checks if an object
class is a subclass of
the class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object
    class is a subclass of the
    class

    Args:
        obj - The object
        a_class - The class to check
    """

    return issubclass(type(obj), a_class)
