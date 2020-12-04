import unittest

from code_editor.core.exceptions.language_exceptions import *
from code_editor.core.executor_facade import CompilerFactory


# Create classes for test
class TestExecutorFacade(unittest.TestCase):
    def test_valid_language(self):
        comp = CompilerFactory()
        self.assertTrue(comp.validate('python'))

    def test_invalid_language_none(self):
        comp = CompilerFactory()
        with self.assertRaises(NoneLanguageException):
            comp.validate(None)

    def test_invalid_language_type_number(self):
        comp = CompilerFactory()
        with self.assertRaises(TypeLanguageException):
            comp.validate(123123)

    def test_invalid_language_type_specialChar(self):
        comp = CompilerFactory()
        with self.assertRaises(TypeLanguageException):
            comp.validate('·$%$·%"')

