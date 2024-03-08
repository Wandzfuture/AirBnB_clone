#!/usr/bin/python3
"""Defines the class FileStorage."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """A class for serializing and deserializing objects to a file>

    Attributes:
        __file_path (str): the name of the file to save objects to.
        __objects (dict): a dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for key, value in objdict.values():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    obj = globals()[cls_name](**value)
                    key = "{}.{}".format(cls_name, value["id"])
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            return
