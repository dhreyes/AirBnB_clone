#!/usr/bin/python3
""" unittest for class BaseModel """
from console import HBNBCommand
import sys
from io import StringIO
import console
import unittest
import pep8
from models.engine.file_storage import all_classes
from unittest.mock import patch, create_autospec
import os
from models import storage


class TestConsole(unittest.TestCase):
    """
    test console code with unit testing
    """
    def testPep8(self):
        """
        check pep8 compliance in console.py as well as unittests
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py',
                                        'tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """
        Sets ups the Test console Unittest by catching in/output
        with a mock object
        """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def session(self):
        """
        creates a console instance
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_create(self):
        """
        Test that create throws proper errors + works w all all_classes
        """
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create asgshsd"))
            self.assertEqual(out.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(out.getvalue(), "** class name missing **\n")
        for cls in all_classes:
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("create {}".format(cls))
                self.assertTrue(len(str(out.getvalue())) == 37)

    def testDestroy(self):
        """
        tests existence of destroy method and validates
        error messages
        """
        my_console = self.session()
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy"))
            self.assertEqual(out.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy Jared"))
            self.assertEqual(out.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy BaseModel"))
            self.assertEqual(out.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy BaseModel 555-ddd"))
            self.assertEqual(out.getvalue(), "** no instance found **\n")
        for cls in all_classes.keys():
            obj = all_classes[cls]()
            key = ".".join([cls, obj.id])
            storage.all()[key] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("destroy {} {}".format(cls, obj.id))
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("show {} {}".format(cls, obj.id))
        for cls in all_classes.keys():
            obj = all_classes[cls]()
            key = ".".join([cls, obj.id])
            storage.all()[key] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd('{}.destroy("{}")'.format(cls, obj.id))
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("show {} {}".format(cls, obj.id))

    def testUpdate(self):
        """
        checks if update command is valid.
        validates all method error messages
        """
        my_console = self.session()
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("update"))
            self.assertEqual(out.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("update Jared"))
            self.assertEqual(out.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("update BaseModel"))
            self.assertEqual(out.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("update BaseModel 4444-"))
            self.assertEqual(out.getvalue(), "** no instance found **\n")
        for cls in all_classes.keys():
            obj = all_classes[cls]()
            key = ".".join([cls, obj.id])
            storage.all()[key] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                cmnd = '{}.update("{}", "passwd", "too short")'
                HBNBCommand().onecmd(cmnd.format(cls, obj.id))
                if 'passwd' in obj.__dict__:
                    self.assertEqual('too short', obj.__dict__['passwd'])
            with patch('sys.stdout', new=StringIO()) as out:
                cmnd = '{}.update("{}", "passwd", "1234")'
                HBNBCommand().onecmd(cmnd.format(cls, obj.id))
                if 'passwd' in obj.__dict__:
                    self.assertEqual('1234', obj.__dict__['passwd'])

    def testCount(self):
        """
        test that count command returns appropriate val
        """
        for k in all_classes.keys():
            count = 0
            for c in storage.all():
                if k in c:
                    count += 1
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("{}.count()".format(k))

    def testShow(self):
        """
        test that validates show command
        """
        for k in all_classes.keys():
            obj = all_classes[k]()
            storage.all()[".".join([k, obj.id])] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("show {} {}".format(k, obj.id))
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd('{}.show("{}")'.format(k, obj.id))

if __name__ == '__main__':
    unittest.main()
