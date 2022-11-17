#!/usr/bin/python3
# class 'Square' that inherits from 'Rectangle' (9-rectangle.py)
"""
    define a Rectangle subclass 'Square'
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        representation of 'Square'
    """

    def __init__(self, size):
        """
            Initialize a new 'Square'
            Args:
                size (int): size of the new square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
