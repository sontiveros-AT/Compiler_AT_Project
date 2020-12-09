#
# @test_executor_facade.py Copyright (c) 2020 Jalasoft.
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

