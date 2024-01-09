#!/usr/bin/python3

"""
Test module for the
rectanle
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test class for the
    Rectangle class
    """

    def test_defualt_id(self):
        """
        Test for id when
        it is none
        """

        rect = Rectangle(10, 4)
        self.assertEqual(rect.id, 1)

    def test_value_passed(self):
        """
        Test when id value
        is passed
        """

        rect = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect.id, 12)
