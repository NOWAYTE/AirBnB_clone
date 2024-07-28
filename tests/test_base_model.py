#!/usr/bin/python3
"""Unittest for base moodel"""
import sys
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestBaseModel(unittest.TestCase):
    def setup(self):
        """Set up """
        self.model = BaseModel(name="Daniel", my_number=50)

    def test_id(self):
        """Test if Id is unique and a string"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)
        self.assertIsInstance(instance1.id, str)
        self.assertEqual(len(instance1.id), 36)
    def test_datetime_att(self):
        """
        Test that two BaseModel instances have different
        datetime object
        """
        first = datetime.now()
        instance1 = BaseModel()
        second = datetime.now()

        self.assertTrue(first <= instance1.created_at <= second)
        self.assertEqual(instance1.created_at, instance1.updated_at)

    def test_to_dict(self):
        """Test values returned from dictionary are correct"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        instance = BaseModel()
        n_dict = instance.to_dict()

        self.assertEqual(type(n_dict['created_at']), str)
        self.assertEqual(type(n_dict['updated_at']), str)
        self.asserEqual(n_dict['__class__'], "BaseModel")
        self.assertEqual(n_dict['created_at'], instance.created_at.strftime(time))
        self.assertEqual(n_dict['updated_at'], instance.updated_at.strftime(time))


if __name__ == "__main__":
    unittest.main()
