#!/usr/bin/python3
"""
unittests for city class
of models
"""

import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City
from models.basemodel import BaseModel


class TestCity(unittest.TestCase):
    """ Unittests for testing the city class """
    def test_id_public(self):
        self.assertEqual(str, type(City().id))

    def test_state_id_
