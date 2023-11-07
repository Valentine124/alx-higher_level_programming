#!/usr/bin/python3

"""
This module contains a
class that inherits from list
and a function that prints the
elements of the list in sorted
form
"""


class MyList(list):
    """
    This is the blueprint
    for my_list objects
    """

    def print_sorted(self):
        """
        prints all the elements
        in a sorted mannar
        """

        print(sorted(self))
