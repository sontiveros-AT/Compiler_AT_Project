import unittest

from code_editor.core.exceptions.parameters_exceptions import NoneParametersException, EmptyParametersException, \
    NotFoundParametersException
from code_editor.core.python.python_parameters import PythonParameters


# Create classes for test
class TestPythonParameters(unittest.TestCase):
    def test_invalid_both_parameters_none(self):
        comp = PythonParameters()
        comp.set_language_path(None)
        comp.set_file_path(None)
        with self.assertRaises(NoneParametersException):
            comp.validate()

    def test_invalid_parameter_file_path_none(self):
        comp = PythonParameters()
        comp.set_language_path('python')
        comp.set_file_path(None)
        with self.assertRaises(NoneParametersException):
            comp.validate()

    def test_invalid_parameter_language_path_none(self):
        comp = PythonParameters()
        comp.set_language_path(None)
        comp.set_file_path('/media/project')
        with self.assertRaises(NoneParametersException):
            comp.validate()

    def test_invalid_both_parameters_empty(self):
        comp = PythonParameters()
        comp.set_language_path('')
        comp.set_file_path('')
        with self.assertRaises(EmptyParametersException):
            comp.validate()

    def test_invalid_parameter_file_path_empty(self):
        comp = PythonParameters()
        comp.set_language_path('python')
        comp.set_file_path('')
        with self.assertRaises(EmptyParametersException):
            comp.validate()

    def test_invalid_parameter_language_path_empty(self):
        comp = PythonParameters()
        comp.set_language_path('')
        comp.set_file_path('/media/project')
        with self.assertRaises(EmptyParametersException):
            comp.validate()

    def test_invalid_both_parameters_nofound(self):
        comp = PythonParameters()
        comp.set_language_path('/media/adsf')
        comp.set_file_path('/media/skadfjasdf')
        with self.assertRaises(NotFoundParametersException):
            comp.validate()
