#!/usr/bin/python3
# function that prints a square with the character #
"""Define 'print_square' function."""


def print_square(size):
    """
        Print a square with the # character.
        Args:
            size (int): height/width of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
