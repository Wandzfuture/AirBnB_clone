#!/usr/bin/python3
"""Defines the class FileStorage."""
import json


class FileStorage:
    """A class for serializing and deserializing objects to a file."""

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
        """Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = {}
                    for k, v in value.items():
                        if k == 'created_at' or k == 'updated_at':
                            v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                        obj_dict[k] = v
                    inst = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = inst
        except FileNotFoundError:
            pass
