#!/usr/bin/python3

"""
This module contains the test
class for the base class
"""


import sys
import unittest
from base import Base

sys.path.append('../..')

class TestBase(unittest.TestCase):
    """
    This class tests the base
    class of our project
    """
    
    def setUp():
