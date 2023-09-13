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

    def to_json(self, attrs=None):
        """
        This function returns the
        dictionary decription of
        the class in attrs

        Args:
            attrs - The attributes to return
        """

        j_dict = {}

        if type(attrs) is list:
            for el in attrs:
                if type(el) is str:
                    for key, value in self.__dict__.items():
                        if el == key:
                            j_dict[key] = value
            return j_dict

        return self.__dict__
