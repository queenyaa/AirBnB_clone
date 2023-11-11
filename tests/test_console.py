#!/usr/bin/python3
"""Unittest for console"""

import unittest
import sys
from models import storage
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_create(self):
        #  Add tests for create command
        pass

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            #  Test case where class name is missing
            self.console.onecmd("show")
            self.assertIn("** class name missing **",
                          mock_stdout.getvalue().strip())

            #  Test case where class doesn't exist
            self.console.onecmd("show UnknownClass")
            self.assertIn("** class doesn't exist **",
                          mock_stdout.getvalue().strip())

            #  Test case where instance id is missing
            self.console.onecmd("show BaseModel")
            self.assertIn("** instance id missing **",
                          mock_stdout.getvalue().strip())

            #  Test case where no instance found
            self.console.onecmd("show BaseModel 123")
            self.assertIn("** no instance found **",
                          mock_stdout.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
