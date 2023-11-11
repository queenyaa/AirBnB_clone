#!/usr/bin/python3
"""
Unittests for the amenity program
"""

import models
import unittest
from models.amenity import Amenity
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Unittests for Amenity """

    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_name(self):
        a = Amenity()
        self.assertIs(type(a.name), str)

    def test_two_amenities(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_name_public(self):
        a = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", a.__dict__)

    def two_amenities_ids(self):
        a1 = Amenity()
        sleep(0.05)
        a2 = Amenity()
        self.assertLess(a1.created_at, a2.created_at)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
