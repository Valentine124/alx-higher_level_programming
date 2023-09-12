#!/usr/bin/python3

"""
This module contains a function
that lookup an object
"""


def lookup(obj):
    """
    This function prints the attributes
    and methods of an object

    Args:
        obj - The object
    """

    return list(obj.__dict__)
