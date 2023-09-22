#!/usr/bin/python3

"""
This module will contain the
base class for for all classes
in this project
"""


class Base:
    """
    This class is the base class
    for all classes in the project
    The goal is to manage id attrribute
    in all future class to avoid
    duplication

    Attribute:
        id - an integer for the id
        __nb_objects - an integer that holds the numbers of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This function initializes the class
        with an id

        Args:
            id - an integer for the id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
