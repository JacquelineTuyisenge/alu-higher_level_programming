#!/usr/bin/python3
# class 'MyList' that inherits from 'list'
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
