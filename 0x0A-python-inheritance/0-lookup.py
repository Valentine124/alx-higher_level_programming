#!/usr/bin/python3

"""
This module contains
a method that prints
a list of all attribute
of an object
"""


def lookup(obj):
    """
    Returns a list of
    all attributes of
    an object

    Args:
        obj - the object
    """

    return dir(obj)
