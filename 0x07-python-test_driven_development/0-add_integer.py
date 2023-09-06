#!/usr/bin/python3

"""
This module defines a single function
that add two integers.
"""


def add_integer(a, b=98):
    """
    This function takes two numbers as
    arguments and return their sum

    Args:
        a - The first number
        b - The second number with default 98
    Return:
        It return the sum of the two numbers
        if they are integers but raises an error
        if any or both are not integer or float
    """

    if a is None or b is None:
        return None

    if not (type(a) is int) and not (type(a) is float):
        raise TypeError("a must be an integer")
    if not (type(b) is int) and not (type(b) is float):
        raise TypeError("b must be an integer")

    sum = int(a) + int(b)

    return sum
