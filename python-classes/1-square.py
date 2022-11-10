#!/usr/bin/python3
# write a class square that defines a square by private attributes
"""
    define a class 'square'
"""


class square:
    """
        square with private insytance attribute: 'size'
    """

    def __init__(self, size):
        """
            Args:
                size (int): size of the new square
        """
        self.__size = size
