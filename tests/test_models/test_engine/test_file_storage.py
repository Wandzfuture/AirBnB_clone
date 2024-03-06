#!/usr/bin/python3
"""
Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Unittests for the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.fs = FileStorage()

    def tearDown(self):
        FileStorage._FileStorage__objects = {}

    def test_FileStorage_instantiation_no_args(self):
        """Test instantiation of FileStorage with no arguments."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """Test instantiation of FileStorage with an argument (not allowed)."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test that __file_path is a private string attribute."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        """Test that __objects is a private dictionary attribute."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """Test that storage is initialized correctly."""
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        """Test the all() method."""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Test the new() method."""
        obj = BaseModel()
        self.fs.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, FileStorage._FileStorage__objects)

    @patch('sys.stdout', new_callable=StringIO)
    def test_save(self, mock_stdout):
        """Test the save() method."""
        obj = BaseModel()
        self.fs.new(obj)
        self.fs.save()
        expected_output = f'"{obj.__class__.__name__}.{obj.id}"\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.open', create=True)
    def test_reload(self, mock_open):
        """Test the reload() method."""
        mock_file = StringIO('{"BaseModel.1": {"id": "1", "name": "test"}}')
        mock_open.return_value = mock_file
        self.fs.reload()
        self.assertIn("BaseModel.1", FileStorage._FileStorage__objects)

    def test_save_with_arg(self):
        """Test save() method with an argument (not allowed)."""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_with_arg(self):
        """Test reload() method with an argument (not allowed)."""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_new_with_args(self):
        """Test new() method with multiple arguments (not allowed)."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)


if __name__ == '__main__':
    unittest.main()
