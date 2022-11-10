#!/usr/bin/python3
# class sqaure that define a square
"""
    define a class 'Square'
"""


class Square:
     """
         square with private instance attribute: 'size'
     """

     def __init__(self, size):
         """
             Args:
                 size (int): size of the new square
         """
         self.size = size

     @property
     def size(self):
         """
             gets current size of the square                                                                     """                             
         return (self.__size)                                     

    @size.setter                                                                                            def size(self, value):                                                                                      """                                                                                                         validates size is an integer that is greater than zero
        """                                                                                                     if not isinstance(value, int):                                                                              raise TypeError("size must be an integer")                                                          elif value < 0:
            raise ValueError("size must be >= 0")                                                               self.__size = value

    def area(self):
        """                                                                                                         Return: area of the square                                                                          """                                                                                                     return (self.__size * self.__size)

    def my_print(self):
        """                                                                                                         prints square with character #                                                                      """
        for i in range(0, self.__size):                                                                             [print("#", end="") for j in range(self.__size)]                                                        print("")                                                                                           if self.__size == 0:
            print("")
