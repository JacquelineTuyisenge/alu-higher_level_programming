#!/usr/bin/python3
# function that returns the JSON,
"""
    define 'to_json_string' function
    import 'json'
"""

import json


def to_json_string(my_obj):
    """
        returns JSON representation of an object(string)
    """

    return json.dumps(my_obj)
