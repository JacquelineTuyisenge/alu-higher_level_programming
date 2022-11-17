#!/usr/bin/python3
# function that writes a string to the text file and
# return the numbers of characters written
"""
    define a function 'write_file'
"""


def write_file(filename="", text=""):
    """
        writes a string to a text file (UTF8)
        and returns the number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
