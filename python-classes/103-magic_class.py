#!/usr/bin/python3
# class that does the same as the output of the sh*ty
"""
   define a class 'MagicClass'
"""


import math


class MagicClass:
    """
       circles
    """

    def __init__(self, radius=0):
        """
           Args:
               radius (float or int): radius of the new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
            Return:
                    area of the MagicClass
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
            Return:
                circumference of the MagicClass
        """
        return (2 * math.pi * self.__radius)
