#!/usr/bin/python3
"""Unittest for base moodel"""
import sys
import os
import unittest
from datetime import datetime
from model.base_model import BaseModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestBaseModel(unittest.Testcase):
    def setup(self):
        """Set up """
        self.model = BaseModel(name="Daniel", my_number=50)

    def test_id(self):
        """Test if Id is unique and a string"""
        self.assertIsInstance(self.model.id, str)
        self.assertEqual(len(self.model.id), 36)
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)
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
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['created_at'], self.model.created_at.strftime(time))
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.strftime(time))


if __name__ == "__main__":
    unittest.main()
