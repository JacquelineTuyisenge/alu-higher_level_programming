#!/usr/bin/python3
"""Defines a base modal class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a base instance"""
        Base.__nb_objects += 1
        self.id = id

    @property
    def id(self):
        """Getter for id"""
        return self.__id

    @id.setter
    def id(self, id):
        """Set id"""
        if id is None:
            self.__id = Base.__nb_objects
        else:
            self.__id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string"""
        if list_dictionaries is None or \
                len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        new_list = []
        if list_objs:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))

        with open(file_name, mode="w") as myFile:
            myFile.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 3)
        elif cls.__name__ == "Square":
            dummy = cls(4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                content = f.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(content)
        list_instances = []
        for dict_instance in list_dicts:
            list_instances.append(cls.create(**dict_instance))
        return list_instances
