#!/usr/bin/python3

"""
This module contains
a function that validate
if an object is an instance
of a specific class
"""


def is_same_class(obj, a_class):
    """
    Return True is the object
    is an instance of the class

    Args:
        obj - The object
        a_class - The class to check
    """

    return type(obj) is a_class
