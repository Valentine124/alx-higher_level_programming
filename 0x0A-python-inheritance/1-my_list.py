#!/usr/bin/python3

"""
This module contains a class that inherits from
the list class and a function thet print the
list in a sorted form
"""


class MyList(list):
    """
    This class inherits from the list class
    """

    def print_sorted(self):
        """
        This function prints the list
        in ascending other
        """

        s = sorted(self)
        print(s)
