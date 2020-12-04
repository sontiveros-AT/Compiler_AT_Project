import unittest

from code_editor.core.exceptions.command_exceptions import NoneCommandException, EmptyCommandException, \
    TypeCommandException
from code_editor.core.python.python_builder_command import PythonBuilderCommand
from code_editor.core.python.python_parameters import PythonParameters


class TestPythonBuilderCommand(unittest.TestCase):
    def test_invalid_command_none(self):
        comp = PythonBuilderCommand()
        with self.assertRaises(NoneCommandException):
            comp.validate(None)

    def test_invalid_command_empty(self):
        comp = PythonBuilderCommand()
        with self.assertRaises(EmptyCommandException):
            comp.validate('')

    def test_invalid_command_type(self):
        comp = PythonBuilderCommand()
        with self.assertRaises(TypeCommandException):
            comp.validate(object)

