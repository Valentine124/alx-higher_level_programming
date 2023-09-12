#!/usr/bin/python3

"""
This module contains a single function
"""


def class_to_json(obj):
    """
    This function returns the dictionary
    description of an object

    Args:
        obj - The object
    """

    return obj.__dict__
