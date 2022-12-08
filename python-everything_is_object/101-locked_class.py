#!/usr/bin/python3
"""
    class 'LockedClass' with no class or object instance that prevents,
    the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
"""


class LockedClass:
    """
        empty LockedClass
    """
    __slots__ = ["first_name"]
