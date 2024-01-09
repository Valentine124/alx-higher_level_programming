#!/usr/bin/python3

"""
The test module
for the base module
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test class for the
    base class
    """

    def test_id_default_value(self):
        """
        Test the defualt
        id value of the
        base class
        """

        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_value_passed(self):
        """
        Test if id is the
        correct value
        """

        base = Base(12)
        self.assertEqual(base.id, 12)

if __name__ == '__main__':
    unittest.main()

