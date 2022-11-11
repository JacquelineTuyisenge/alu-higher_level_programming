#!/usr/bin/python3
# class square thatdefines a square
"""
    define a class 'Square'
"""


class Square:
    """
        square with private instance attribute: 'size'
    """

    def __init__(self, size=0, position=(0, 0)):
        """
            Args:
                size (int): size of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
            gets current size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
            validates size is an integer that is greater than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
            gets the current position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
           set position
           Args:
               value: position of the square
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
            Return: area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
            prints square with character #
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """
            define the print() representation of a square
        """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
