#!/usr/bin/python3

"""
This module contains the
base class
"""


class Base:
    """
    The base class
    for all shapes

    Attributes:
        __nb_objects - the number of object created
        id - the id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
