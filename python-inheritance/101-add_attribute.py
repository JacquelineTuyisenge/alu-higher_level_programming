#!/usr/bin/python3
# function that adds a new attribute to an object if it’s possible
"""
    define a function 'add_attribute'
"""


def add_attribute(obj, name, value):
    """
        add a new attribute to an object if possible
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
