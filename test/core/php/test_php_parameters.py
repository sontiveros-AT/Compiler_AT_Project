#
# @test_php_parameters.py Copyright (c) 2020 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 subsuelo Edif. La Unión, Av. Gral. Inofuentes, Calacoto, La Paz, Bolivia
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the termns of the license agreement you entered into
# with Jalasoft.
#
# Author: Alvaro Cruz
# Version: 1.0
#

import unittest
from code_editor.core.exceptions.parameters_exceptions import NoneParametersException
from code_editor.core.exceptions.parameters_exceptions import EmptyParametersException
from code_editor.core.exceptions.parameters_exceptions import NotFoundParametersException
from code_editor.core.php.php_parameters import PhpParameters


# Create classes for test
class TestPhpParameters(unittest.TestCase):
    # def test_valid_both_parameters(self):
    #     comp = PhpParameters()
    #     comp.set_language_path('C:\Tests\CompilerProjectBugFix\Compiler_AT_Project/third_parties/php/php7.4.11/php.exe')
    #     comp.set_file_path('C:\Tests\CompilerProjectBugFix\Compiler_AT_Project/media/808eb9893815d1931afaea1dfe57dfb6/php/7.4.11/projectphp/main.php')
    #     self.assertTrue(comp.validate())

    def test_invalid_both_parameters_none(self):
        comp = PhpParameters()
        comp.set_language_path(None)
        comp.set_file_path(None)
        with self.assertRaises(NoneParametersException):
            comp.validate()

    def test_invalid_parameter_file_path_none(self):
        comp = PhpParameters()
        comp.set_language_path('python')
        comp.set_file_path(None)
        with self.assertRaises(NoneParametersException):
            comp.validate()

    def test_invalid_parameter_language_path_none(self):
        comp = PhpParameters()
        comp.set_language_path(None)
        comp.set_file_path('/media/project')
        with self.assertRaises(NoneParametersException):
            comp.validate()

    def test_invalid_both_parameters_empty(self):
        comp = PhpParameters()
        comp.set_language_path('')
        comp.set_file_path('')
        with self.assertRaises(EmptyParametersException):
            comp.validate()

    def test_invalid_parameter_file_path_empty(self):
        comp = PhpParameters()
        comp.set_language_path('python')
        comp.set_file_path('')
        with self.assertRaises(EmptyParametersException):
            comp.validate()

    def test_invalid_parameter_language_path_empty(self):
        comp = PhpParameters()
        comp.set_language_path('')
        comp.set_file_path('/media/project')
        with self.assertRaises(EmptyParametersException):
            comp.validate()

    def test_invalid_both_parameters_nofound(self):
        comp = PhpParameters()
        comp.set_language_path('/third_parties/c++')
        comp.set_file_path('/media/project')
        with self.assertRaises(NotFoundParametersException):
            comp.validate()
