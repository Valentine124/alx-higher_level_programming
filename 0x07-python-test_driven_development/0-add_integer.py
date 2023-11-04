#!/usr/bin/python3

"""
This module contains the
add function
"""


def add_integer(a, b=98):
    if not (type(a) is int) and not (type(a) is float):
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    ai = int(a)
    bi = int(b)

    return ai + bi
