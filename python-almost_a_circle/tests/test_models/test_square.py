#!/usr/bin/python3

import os
import unittest
from models.base import Base
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """Test class for square"""

    def test_instance(self):
        """Test for instance"""
        Base._Base__nb_objects = 0
        s = Square(1)
        s1 = Square(1, 2)
        s2 = Square(1, 2, 3)
        s3 = Square(1, 0)
        s4 = Square(1, 2, 3, 4)

        self.assertEqual(s3.id, 4)
        self.assertEqual(s4.id, 4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s5 = Square(-1, 2)
        
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
              s6 = Square(1, -2)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s7 = Square(0, 2)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s8 = Square(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s9 = Square(0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s10 = Square("1")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s11 = Square(1, "2")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s12 = Square(1, 2, "3")

    def test_area(self):
        """Test for area function"""
        Base._Base__nb_objects = 0
        self.assertEqual(Square(2).area(), 4)

    def test___str__(self):
        """Test for __str__ function"""
        Base._Base__nb_objects = 0
        s = Square(1)
        with patch('sys.stdout', new=StringIO()) as f:
            print(s)
            self.assertEqual(f.getvalue(), "[Square] (1) 0/0 - 1\n")

    def test_display(self):
        """Test for display function"""
        u1 = Square(2)
        u2 = Square(2, 2, 3)
        with patch('sys.stdout', new=StringIO()) as f:
            u1.display()
            self.assertEqual(f.getvalue(), "##\n##\n")

        with patch('sys.stdout', new=StringIO()) as f:
            u2.display()
            self.assertEqual(f.getvalue(), "\n\n\n  ##\n  ##\n")

    def test_dictionary(self):
        """Test for to_dictionary function"""
        Base._Base__nb_objects = 0
        s = Square(4)
        s_dictionary = s.to_dictionary()
        self.assertEqual(s_dictionary, {'x': 0, 'y': 0, 'id': 1, 'size': 4})

    def test_update(self):
        """Test for update function"""
        Base._Base__nb_objects = 0
        s = Square(1)
        self.assertEqual(s.id, 1)

        s.update(89)
        self.assertEqual(s.id, 89)

        s.update(89, 1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.id, 89)

        s.update(89, 1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.id, 89)

        s.update(89, 1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 89)

        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        self.assertEqual(s.id, 89)

        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.id, 89)

        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 89)

    def test_create(self):
        """Test for create function"""

        c1 = Square.create(**{'id': 89})
        self.assertEqual(c1.id, 89)

        c2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(c2.size, 1)
        self.assertEqual(c2.id, 89)

        c3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(c3.size, 1)
        self.assertEqual(c3.x, 2)
        self.assertEqual(c3.id, 89)

        c4 = Square.create(**{'id': 89, 'size': 1,
        'x': 2, 'y': 3})
        self.assertEqual(c4.size, 1)
        self.assertEqual(c4.x, 2)
        self.assertEqual(c4.y, 3)
        self.assertEqual(c4.id, 89)

    def test_save_to_file(self):
        """Test for save to file function"""
        Base._Base__nb_objects = 0

        Square.save_to_file(None)
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(type(f.read()), str)

        Square.save_to_file([Square(1)])
        with open("Square.json") as f:
            self.assertEqual(f.read(),
            '[{"id": 1, "size": 1, "x": 0, "y": 0}]')

    def test_save_to_file_empty(self):
        """Test for save to file function"""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(type(f.read()), str)

    def test_save_from_file(self):
        """Test for save from file function"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([Square(2)])
        file = Square.load_from_file()
        self.assertEqual(type(file), list)
        self.assertEqual(file[0].size, 2)

if __name__ == '__main__':
    unittest.main()
