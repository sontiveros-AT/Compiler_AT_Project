import unittest

from code_editor.core.exceptions.language_exceptions import *
from code_editor.core.executor_facade import CompilerFactory


class TestExecutorFacade(unittest.TestCase):
    def test_invalid_language_none(self):

        comp = CompilerFactory()
        with self.assertRaises(NoneLanguageException):
            comp.validate(None)

    def test_invalid_language_type(self):

        comp = CompilerFactory()
        with self.assertRaises(TypeLanguageException):
            comp.validate(123123)

    def test_invalid_language_nofound(self):

        comp = CompilerFactory()
        with self.assertRaises(FoundLanguageException):
            comp.validate('php')
