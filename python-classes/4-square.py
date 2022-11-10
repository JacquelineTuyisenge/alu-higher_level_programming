#!/usr/bin/python3
# defines a square by private instance attribute 'size'
"""
    define a class 'Square'
"""


class Square:
    """
        square with private instance attribute: 'size'
    """

    def __init__(self, size=0):
        """
            Args:
                size (int): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            Return: area of the square
        """
        return (self.__size * self.__size)

    
