#!/usr/bin/python3
# function that prints 'My name is <first name> <last name>'
"""Define 'say_my_name'  function."""


def say_my_name(first_name, last_name=""):
    """
        print a name.
        Args:
             first_name (str): first name to print.
             last_name (str): last name to print.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
