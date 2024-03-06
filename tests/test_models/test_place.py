#!/usr/bin/python3
"""
Defines unittests for models/place.py.

Unittest classes:
    TestPlace
"""
import os
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instantiation(self):
        """Test Place instantiation."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """Test Place attributes."""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_attributes_default_values(self):
        """Test default values for Place attributes."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes_types(self):
        """Test types for Place attributes."""
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_str_representation(self):
        """Test str representation of Place."""
        place = Place()
        self.assertIn("[Place]", str(place))
        self.assertIn("id:", str(place))
        self.assertIn("created_at:", str(place))
        self.assertIn("updated_at:", str(place))

    def test_created_at_and_updated_at_attributes(self):
        """Test created_at and updated_at attributes."""
        place = Place()
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_to_dict_method(self):
        """Test to_dict method of Place."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('id', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)
        self.assertIn('__class__', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)

    def test_save_method(self):
        """Test save method of Place."""
        place = Place()
        created_at = place.created_at
        updated_at = place.updated_at
        place.save()
        self.assertNotEqual(updated_at, place.updated_at)
        self.assertEqual(created_at, place.created_at)

    def test_kwargs_constructor(self):
        """Test kwargs constructor of Place."""
        data = {
            'id': 'test_id',
            'city_id': 'test_city_id',
            'user_id': 'test_user_id',
            'name': 'test_name',
            'description': 'test_description',
            'number_rooms': 5,
            'number_bathrooms': 3,
            'max_guest': 8,
            'price_by_night': 100,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenity_ids': ['test_amenity_id1', 'test_amenity_id2'],
            'created_at': '2024-03-06T00:00:00',
            'updated_at': '2024-03-06T00:00:00',
        }
        place = Place(**data)
        self.assertEqual(place.id, 'test_id')
        self.assertEqual(place.city_id, 'test_city_id')
        self.assertEqual(place.user_id, 'test_user_id')
        self.assertEqual(place.name, 'test_name')
        self.assertEqual(place.description, 'test_description')
        self.assertEqual(place.number_rooms, 5)
        self.assertEqual(place.number_bathrooms, 3)
        self.assertEqual(place.max_guest, 8)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, [
            'test_amenity_id1',
            'test_amenity_id2'
        ])
        self.assertEqual(place.created_at, datetime(2024, 3, 6, 0, 0, 0))
        self.assertEqual(place.updated_at, datetime(2024, 3, 6, 0, 0, 0))


if __name__ == "__main__":
    unittest.main()
