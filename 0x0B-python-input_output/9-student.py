#!/usr/bin/python3

"""
This module contains a class
``Student``
"""


class Student:
    """
    This class create a student type

    Attributes:
        first_name - the student first name
        last_name - The student last name
        age - the student age
    """

    def __init__(self, first_name, last_name, age):
        """
        The student initializer

        Args:
            first_name - the student first name
            last_name - The student last name
            age - the student age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This function returns the
        dictionary decription of
        the class
        """

        return self.__dict__
