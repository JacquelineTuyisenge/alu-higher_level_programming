#!/usr/bin/python3
# write a class square that defines a square
"""
    define a class 'square'
"""


class square:
    """
        square with private instance attribute: 'size'
    """

    def __init__(self, size=0):
        """
            Args:
                size (init): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            Return: area of the square
        """
        return (self.__size * self.__size)
