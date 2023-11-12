#!/usr/bin/python3
"""
Unittesting the review class
"""

import models
import unittest
from datetime import datetime
import os
from time import sleep
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Unittesting for the Review class
    """
    def test_new_inst_stored(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_place_id_public(self):
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_unique_review(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_str_repr(self):
        d_time = datetime.now()
        d_time_r = repr(d_time)
        rev = Review()
        rev.id = "8602393"
        rev.created_at = rev.updated_at = d_time
        rev_str = rev.__str__()
        self.assertIn("[Review] (8602393)", rev_str)
        self.assertIn("'created_at': " + d_time_r, rev_str)
        self.assertIn("'updated_at': " + d_time_r, rev_str)

    def test_inst_with_kwargs(self):
        d_time = datetime.now()
        d_time_i = d_time.isoformat()
        rev = Review(id="861", created_at=d_time_i, updated_at=d_time_i)
        self.assertEqual(rev.id, "861")
        self.assertEqual(rev.created_at, d_time)
        self.assertEqual(rev.updated_at, d_time)


if '__name__' == '__main__':
    unittest.main()
