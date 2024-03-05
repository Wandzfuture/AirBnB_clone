#!/usr/bin/python3
"""Defines unit tests for FileStorage class."""
import unittest
import json
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_all(self):
        """Test the all method."""
        storage.new(BaseModel())
        objects = storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """Test the new method."""
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all())

    def test_save(self):
        """Test the save method."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key, data)

    def test_reload(self):
        """Test the reload method."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all())


if __name__ == '__main__':
    unittest.main()
