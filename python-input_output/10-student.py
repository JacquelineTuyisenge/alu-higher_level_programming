#!/usr/bin/python3
# Write a class Student that defines a student
# (based on 9-student.py)
"""
    class 'Student'
"""


class Student:
    """
        define class 'Student'
    """

    def __init__(self, first_name, last_name, age):
        """
            init a new Student
        """

    self.first_name = first_name
    self.last_name = last_name
    self.age = age
def to_json(self, attrs=None):
    """
        retrieve dictionary representation of a Student instance
    """

    if attrs is None or type(attrs) is not list:
        return self.__dict__
    for att in attrs:
        if type(att) is not str:
            return self.__dict__
    return {x: self.__dict__[x] for x in self.__dict__ if x in attrs}
