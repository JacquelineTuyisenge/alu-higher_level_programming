#!/usr/bin/python3
# class "MyInt' that inherits from 'init'
"""
    define a class 'MyInt' inheriting from 'int'
"""


class MyInt(int):
    """
        invert int operators '==' and '!='
    """

    def __eq__(self, value):
        """
            override '==' opeartor with '!='
        """

        return self.real != value

    def __ne__(self, value):
        """
            override '!=' operator with '=='
        """

        return self.real == value
