#
# @test_java_builder_command.py Copyright (c) 2020 Jalasoft.
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
from code_editor.core.exceptions.command_exceptions import NoneCommandException
from code_editor.core.exceptions.command_exceptions import EmptyCommandException
from code_editor.core.exceptions.command_exceptions import TypeCommandException
from code_editor.core.java.java_builder_command import JavaBuilderCommand
from code_editor.core.java.java_parameters import JavaParameters


class TestJavaBuilderCommand(unittest.TestCase):
    # def test_valid_command(self):
    #     params = JavaParameters()
    #     params.set_language_path('C:\Tests\CompilerProjectBugFix\Compiler_AT_Project/third_parties/java/jdk-13.0.2/bin')
    #     params.set_file_path('C:\Tests\CompilerProjectBugFix\Compiler_AT_Project/media/808eb9893815d1931afaea1dfe57dfb6/java/13.0.2/projectjava/src/com/Main.java')
    #     comp = JavaBuilderCommand()
    #     self.assertTrue(comp.validate(params))

    def test_invalid_command_none(self):
        comp = JavaBuilderCommand()
        with self.assertRaises(NoneCommandException):
            comp.validate(None)

    def test_invalid_command_empty(self):
        comp = JavaBuilderCommand()
        with self.assertRaises(EmptyCommandException):
            comp.validate('')

    def test_invalid_command_type(self):
        comp = JavaBuilderCommand()
        with self.assertRaises(TypeCommandException):
            comp.validate(object)
