#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 5, 3, 2]), 5)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)
        self.assertEqual(max_integer([-10, -20, -5]), -5)
        self.assertEqual(max_integer([-1, 5, -3, 2]), 5)
        self.assertEqual(max_integer([0, -5, 10, -20]), 10)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 2.1]), 3.9)
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-5, 0, -1]), 0)
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertIsNone(max_integer([]))
