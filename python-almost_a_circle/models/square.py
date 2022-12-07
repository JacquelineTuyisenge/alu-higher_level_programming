#!/usr/bin/python3
# class Square that inherits from Rectangle
"""A rectangle module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of a square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the attributes of a square"""
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
