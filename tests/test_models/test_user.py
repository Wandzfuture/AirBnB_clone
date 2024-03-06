#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instantiation(self):
        """Test State instantiation."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Test State attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_attributes_default_values(self):
        """Test default values for State attributes."""
        state = State()
        self.assertEqual(state.name, "")

    def test_attributes_types(self):
        """Test types for State attributes."""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_str_representation(self):
        """Test str representation of State."""
        state = State()
        self.assertIn("[State]", str(state))
        self.assertIn("id:", str(state))
        self.assertIn("created_at:", str(state))
        self.assertIn("updated_at:", str(state))

    def test_created_at_and_updated_at_attributes(self):
        """Test created_at and updated_at attributes."""
        state = State()
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_to_dict_method(self):
        """Test to_dict method of State."""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('id', state_dict)
        self.assertIn('name', state_dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)

    def test_save_method(self):
        """Test save method of State."""
        state = State()
        created_at = state.created_at
        updated_at = state.updated_at
        state.save()
        self.assertNotEqual(updated_at, state.updated_at)
        self.assertEqual(created_at, state.created_at)

    def test_kwargs_constructor(self):
        """Test kwargs constructor of State."""
        data = {
            'id': 'test_id',
            'name': 'test_name',
            'created_at': '2024-03-06T00:00:00',
            'updated_at': '2024-03-06T00:00:00',
        }
        state = State(**data)
        self.assertEqual(state.id, 'test_id')
        self.assertEqual(state.name, 'test_name')
        self.assertEqual(state.created_at, datetime(2024, 3, 6, 0, 0, 0))
        self.assertEqual(state.updated_at, datetime(2024, 3, 6, 0, 0, 0))

    def test_invalid_kwarg(self):
        """Test instantiation with invalid kwargs."""
        with self.assertRaises(TypeError):
            State(invalid_arg='test')

    def test_add_state(self):
        """Test adding a new state."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_update_state(self):
        """Test updating an existing state."""
        state = State()
        state.name = "New York"
        state.save()
        state.name = "NY"
        self.assertEqual(state.name, "NY")

    def test_delete_state(self):
        """Test deleting a state."""
        state = State()
        state.name = "Texas"
        state.save()
        state.delete()
        self.assertNotIn(state, State.all())

    def test_multiple_states(self):
        """Test handling multiple states."""
        state1 = State()
        state1.name = "Florida"
        state1.save()
        state2 = State()
        state2.name = "Georgia"
        state2.save()
        states = State.all()
        self.assertIn(state1, states)
        self.assertIn(state2, states)

    def test_empty_state(self):
        """Test creating an empty state."""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
