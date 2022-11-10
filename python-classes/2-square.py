#!/usr/bin/python3
# write a class square that defines a square by private instance attribute 'size'
"""
    define a class 'square'
"""

def __init__(self, size=0):
    """
        Args:
            size (init): size of the new square
    """
    if not isinstance(size, int):
        raise TypeError("size must be integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
