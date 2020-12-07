#
# @test_php_builder_command.py Copyright (c) 2020 Jalasoft.
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
from code_editor.core.exceptions.command_exceptions import NoneCommandException, EmptyCommandException, \
    TypeCommandException
from code_editor.core.php.php_builder_command import PhpBuilderCommand
from code_editor.core.php.php_parameters import PhpParameters


class TestPhpBuilderCommand(unittest.TestCase):
    def test_valid_command(self):
        params = PhpParameters()
        params.set_language_path('C:\Tests\CompilerProjectBugFix\Compiler_AT_Project/third_parties/php/php7.4.11/php.exe')
        params.set_file_path('C:\Tests\CompilerProjectBugFix\Compiler_AT_Project/media/808eb9893815d1931afaea1dfe57dfb6/php/7.4.11/projectphp/main.php')
        comp = PhpBuilderCommand()
        self.assertTrue(comp.validate(params))

    def test_invalid_command_none(self):
        comp = PhpBuilderCommand()
        with self.assertRaises(NoneCommandException):
            comp.validate(None)

    def test_invalid_command_empty(self):
        comp = PhpBuilderCommand()
        with self.assertRaises(EmptyCommandException):
            comp.validate('')

    def test_invalid_command_type(self):
        comp = PhpBuilderCommand()
        with self.assertRaises(TypeCommandException):
            comp.validate(object)

