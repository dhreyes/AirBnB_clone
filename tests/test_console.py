#!/usr/bin/python3
""" unittest for class BaseModel """
import unittest
from models.base_model import BaseModel
import pep8


class TestConsole(unittest.TestCase):
    """ tests stuff in unittest standard """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py',
                                        'tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
