#!/usr/bin/python3
"""Defines FileStorage module"""
import json
import os
import ast

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and
       deserializes JSON file to instances
    """
    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self) -> dict:
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_key: str = obj.__class__.__name__ + "." + obj.id
        self.__objects[obj_key] = obj

    def delete(self, key) -> None:
        """Deletes an object from __objects dict"""
        del self.__objects[key]

    def update(self, key, attribute_name, attribute_value) -> None:
        """Updates an object of __objects dict"""
        try:
            attribute_value = ast.literal_eval(attribute_value)
        except (ValueError, SyntaxError):
            pass
        setattr(self.__objects[key], attribute_name, attribute_value)

    def save(self) -> None:
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            new_dict = {key: obj.to_dict() for key, obj
                        in self.__objects.items()}
            json.dump(new_dict, file)

    def reload(self) -> None:
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                new_dict = json.load(file)
                for key, val in new_dict.items():
                    self.__objects[key] = eval(val['__class__'])(**val)
