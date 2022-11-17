#!/usr/bin/python3
# rectangle inherits from basegeometry
"""
    define a class 'Rectangle' inheriting from 'BaseGeometry'
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        representation of 'Rectangle'
    """

    def __init__(self, width, heights):
        """
            intialize a new 'Rectangle'
            Args:
                width (int): width of the new rectangle
                height (int): height of the new rectangle
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
            Return: area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
            Return: print() & str() representation of a 'Rectangle'
        """

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
