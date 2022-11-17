#!/usr/bin/python3
# function that writes an Object to a text file,
"""
    define a function 'save_to_json_file'
    import 'json'
"""

import json


def save_to_json_file(my_obj, filename):
    """
        writes an object to a text file, using json representation
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
