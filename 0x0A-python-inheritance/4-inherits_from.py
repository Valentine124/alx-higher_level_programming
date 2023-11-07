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

    clss = type(obj)

    if (clss is a_class):
        return False

    return issubclass(clss, a_class)
