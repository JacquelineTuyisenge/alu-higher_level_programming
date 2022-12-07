#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_ordered_list(self):
        """Test ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)
    
    def test_max_at_beginning(self):
        """Test max at beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_one_element(self):
        """Test one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test floats"""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
        """Test ints and floats"""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test_string(self):
        """Test string"""
        self.assertEqual(max_integer("Holberton"), 't')

    def test_list_of_strings(self):
        """Test list of strings"""
        self.assertEqual(max_integer(["Holberton", "School", "Hi"]), "School")

    def test_empty_string(self):
        """Test empty string"""
        self.assertEqual(max_integer(""), None)
    
if __name__ == '__main__':
    unittest.main()
