#
# @validate.py Copyright (c) 2020 Jalasoft.
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

import os

from code_editor.core.exceptions.language_exceptions import *


class Validate:
    @staticmethod
    def validate_language(language):
        if language is None:
            raise NoneLanguageException(language)
        elif type(language) == int or type(language) == float:
            raise TypeLanguageException(language)
        elif not language.isalpha():
            raise TypeLanguageException(language)
        elif language.lower().strip() != 'python' and language.lower().strip() != 'java':
            raise FoundLanguageException(language)
        return True

    # @staticmethod
    # def validate_path(file_path):
    #     if file_path is None:
    #         raise NonePathFileException(file_path)
    #     elif not os.path.isfile(file_path):
    #         raise NoFoundPathFileException(file_path)
    #     return True
    #
    # @staticmethod
    # def validate_compiler_python(python_compiler_path):
    #     if not os.path.isfile(python_compiler_path):
    #         raise NoFoundCompilerException(python_compiler_path)
    #     return True
