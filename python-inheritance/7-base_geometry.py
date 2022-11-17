#!/usr/bin/python3
#  class BaseGeometry (based on 6-base_geometry.py).
"""
     define a class 'BaseGeometry'
"""


class BaseGeometry:
    """
        Representation of 'BaseGeometry'
    """

    def area(self):
        """
        raises Exception with message
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
            validate value as a positive integer
        """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
