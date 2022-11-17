#!/usr/bin/python3
# class 'square' that inherits from 'Rectangle'
"""
    define a class 'Square' inheriting from 'BaseGeometry'
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        representation of 'Square
    """

    def __init__(self, size):
        """
            instantiate private instance field size
        """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
