#
# @executor_facade.py Copyright (c) 2020 Jalasoft.
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

from code_editor.core.exceptions.language_exceptions import *
from code_editor.core.javascript.javascript_executor import JavascriptExecutor
from code_editor.core.php.php_executor import PhpExecutor
from code_editor.core.python.python_executor import PythonExecutor
from code_editor.core.java.java_executor import JavaExecutor


# Class that instantiates the request language
class CompilerFactory:
    languages = {'python': PythonExecutor(), 'java': JavaExecutor(), 'javascript': JavascriptExecutor(),
                 'php': PhpExecutor()}

    def create_compiler(self, language):
        self.validate(language)
        executor = self.languages[language]
        return executor

    def validate(self, language):
        if language is None:
            raise NoneLanguageException(language)
        elif type(language) == int or type(language) == float:
            raise TypeLanguageException(language)
        elif not language.isalpha():
            raise TypeLanguageException(language)
