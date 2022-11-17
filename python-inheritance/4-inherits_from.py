#!/usr/bin/python3
# return 'true' if object is instance of class
#that inherits directly or indirectly from
# specified class ; otherwise 'False'
"""
    define a function 'inherits_from"
"""


def inherits_from(obj, a_class):
    """
        checks if an object is an inherited instance of a class
        Return: -True
                - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

