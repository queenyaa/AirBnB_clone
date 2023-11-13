#!/usr/bin/python3

"""
unittesting how FileStorage class work
with all other classes
"""

import models
from datetime import datetime
import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ class to test File storage class"""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        # test all storage
        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict, {})

    def test_variables(self):
        # testing variables of class
        f1 = FileStorage()
        list_them = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for ex in f1.all().values():
            list_them.append(ex)
        for ex in list_them:
            del f1.all()[ex.__class__.__name__ + '.' + ex.id]

        self.assertFalse(hasattr(FileStorage, '__file_path'))
        self.assertFalse(hasattr(FileStorage, '__objects'))
        self.assertFalse(hasattr(f1, '__file_path'))
        self.assertFalse(hasattr(f1, '__objects'))
        del f1
        if os.path.exists('file.json'):
            print('file still exists')
            os.remove('file.json')

    def test_new(self):
        # test for new User
        user = User()
        self.storage.new(user)
        obj_dict = self.storage.all()
        self.assertEqual(len(obj_dict), 1)
        self.assertIn("User." + user.id, obj_dict)

    def test_save_file_existence(self):
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))


if __name__ == '__main__':
    unittest.main()
