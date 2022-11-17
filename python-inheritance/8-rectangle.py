#!/usr/bin/python3
# Rectangle class that inherits from
# BaseGeometry
"""
    define a class 'Rectangle' inheriting from 'BaseGeometry'
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        representation of 'Rectangle'
    """

    def __init__(self, width, height):
        """
            intialize a new 'Rectangle'
            Args:
                width (int): width of the new rectangle
                height (int): height of the new rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
