#!/usr/bin/python3
# Write a function that returns the dictionary description with simple data
# structure (list, dictionary, string, integer and boolean) for JSON
# serialization of an object
"""
    define a function 'class_to_json'
"""


def class_to_json(obj):
    """
        return dictionary description for JSON object
    """

    return obj.__dict__
