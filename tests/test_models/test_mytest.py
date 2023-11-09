#!/usr/bin/python3
"""
unittest to test the BaseModel function
"""

import unittest
import models
import os
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    """
    Class to test the BaseModel Function
    """

    def test_init_no_args(self):
        # Testing initialization with args
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_public_id(self):
        # checks if id is public
        self.assertEqual(str, type(BaseModel().id))

    def test_public_created_at_datetime(self):
        # checks if created datetime is public
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_init_with_kwargs(self):
        # Testing BaseModel initialization with kwargs
        data = {
                'id': str(uuid.uuid4()),
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat(),
                'name': 'TestingObj'
        }
        obj = BaseModel(**data)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(hasattr(obj, 'name'))
        self.assertEqual(obj.id, data['id'])
        self.assertEqual(obj.name, data['name'])
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_without_kwargs(self):
	# Testing initialization without kwargs
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.updated_at, datetime)

    def test_two_unique_ids(self):
        # Tests if two ids are unique
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_save_method(self):
        # Testing the saving method
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        # Testing the saving method
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_str_method(self):
        # Testing the __str__ method
        obj_dt = datetime.now()
        obj_dt_r = repr(obj_dt)

        obj = BaseModel()
        obj.id = "8602393"
        obj.created_at = obj.updated_at = obj_dt

        obj_str = str(obj)

        self.assertIn("[BaseModel] (8602393)", obj_str)
        self.assertIn("'id': '8602393'", obj_str)
        self.assertIn("'created_at': " + obj_dt_r, obj_str)
        self.assertIn("'updated_at': " + obj_dt_r, obj_str)


if __name__ == '__main__':
	unittest.main()
