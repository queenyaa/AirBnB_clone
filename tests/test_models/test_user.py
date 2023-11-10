#!/usr/bin/python3
"""
Unittest to test the user class
"""

import unittest
import models
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """testing the User class"""

    def test_no_args(self):
        # test that there are no args
        self.assertEqual(User, type(User()))

    def test_instance_stored_in_obj(self):
        # test stored users
        self.assertIn(User(), models.storage.all().values())

    def test_id_public(self):
        # test if the id is a public string
        self.assertEqual(str, type(User().id))

    def test_attributes(self):
        # testing attributes
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_to_dict_method(self):
        # test the dict method
        user = User()
        user_dict = user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], user.id)
        self.assertEqual(user_dict['created_at'], user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], user.updated_at.isoformat())
        self.assertEqual(user_dict['email'], user.email)
        self.assertEqual(user_dict['password'], user.password)
        self.assertEqual(user_dict['first_name'], user.first_name)
        self.assertEqual(user_dict['last_name'], user.last_name)

    def test_str_representation(self):
        # test the str representation
        user = User()
        user.id ="8602393"
        user.created_at = user.update_at = datetime(2023, 11, 9, 9, 0, 0)
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "Abu"
        user.last_name = "Farakan"

        user_str = str(user)
        self.assertIn("[User] (8602393)", user_str)
        self.assertIn("'id': '8602393'", user_str)
        self.assertIn("'created_at': '2023-11-09T09:00:00;", user_str)
        self.assertIn("'updated_': '2023-11-09T09:00:00'", user_str)
        self.assertIn("'email': 'test@example.com'", user_str)
        self.assertIn("'password': 'password123'", user_str)
        self.assertIn("'first_name': 'Abu'", user_str)
        self.assertIn("'last_name': 'Farakan'", user_str)


if __name__ == '__main__':
    unittest.main()
