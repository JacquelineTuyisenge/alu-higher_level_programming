#!/usr/bin/python3
# return the list of available attributes and methds of an object
"""
    define a class 'MyList'
"""


class MyList(list):
    """
        implement sorted list
    """

    def print_sorted(self):
        """
            prints sorted list
        """
        print(sorted(self))
