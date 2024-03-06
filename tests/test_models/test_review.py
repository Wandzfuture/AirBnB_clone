#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview
    ...tests save/delete/update/to_dict/str/instantiation/
    attributes/attributes_default_values/attributes_types/
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
import os


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instantiation(self):
        """Test Review instantiation."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test Review attributes."""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_attributes_default_values(self):
        """Test default values for Review attributes."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes_types(self):
        """Test types for Review attributes."""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_str_representation(self):
        """Test str representation of Review."""
        review = Review()
        self.assertIn("[Review]", str(review))
        self.assertIn("id:", str(review))
        self.assertIn("created_at:", str(review))
        self.assertIn("updated_at:", str(review))

    def test_created_at_and_updated_at_attributes(self):
        """Test created_at and updated_at attributes."""
        review = Review()
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_to_dict_method(self):
        """Test to_dict method of Review."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('id', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)
        self.assertIn('__class__', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

    def test_save_method(self):
        """Test save method of Review."""
        review = Review()
        created_at = review.created_at
        updated_at = review.updated_at
        review.save()
        self.assertNotEqual(updated_at, review.updated_at)
        self.assertEqual(created_at, review.created_at)

    def test_kwargs_constructor(self):
        """Test kwargs constructor of Review."""
        data = {
            'id': 'test_id',
            'place_id': 'test_place_id',
            'user_id': 'test_user_id',
            'text': 'test_text',
            'created_at': '2024-03-06T00:00:00',
            'updated_at': '2024-03-06T00:00:00',
        }
        review = Review(**data)
        self.assertEqual(review.id, 'test_id')
        self.assertEqual(review.place_id, 'test_place_id')
        self.assertEqual(review.user_id, 'test_user_id')
        self.assertEqual(review.text, 'test_text')
        self.assertEqual(review.created_at, datetime(2024, 3, 6, 0, 0, 0))
        self.assertEqual(review.updated_at, datetime(2024, 3, 6, 0, 0, 0))

    def test_invalid_kwarg(self):
        """Test instantiation with invalid kwargs."""
        with self.assertRaises(TypeError):
            Review(invalid_arg='test')

    def test_multiple_reviews(self):
        """Test creation of multiple reviews."""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_update_review_text(self):
        """Test updating review text."""
        review = Review()
        original_text = review.text
        new_text = "Updated review text"
        review.text = new_text
        self.assertEqual(review.text, new_text)
        self.assertNotEqual(review.text, original_text)

    def test_empty_review_text(self):
        """Test empty review text."""
        review = Review()
        review.text = ""
        self.assertEqual(review.text, "")

    def test_review_text_length(self):
        """Test review text length."""
        review = Review()
        review.text = "a" * 1001
        self.assertEqual(len(review.text), 1000)

    def test_review_creation_timestamps(self):
        """Test review creation timestamps."""
        review = Review()
        self.assertEqual(review.created_at, review.updated_at)

    def test_review_update_timestamps(self):
        """Test review update timestamps."""
        review = Review()
        created_at = review.created_at
        review.text = "Updated review text"
        self.assertNotEqual(created_at, review.updated_at)


if __name__ == "__main__":
    unittest.main()
