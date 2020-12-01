#
# @python_executor.py Copyright (c) 2020 Jalasoft.
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

import subprocess

from code_editor.core.exceptions.exceptions import ExecuteInvalidException
from code_editor.core.executor import Executor
from code_editor.core.javascript.javascript_builder_command import JavascriptBuilderCommand
from code_editor.core.javascript.javascript_parameters import JavascriptParameters
from code_editor.core.path_compiler import PathCompiler
from code_editor.core.settings import BASE_DIR, JAVASCRIPT14_PATH


# Class to execute Python commands
class JavascriptExecutor(Executor):

    def __init__(self):
        self.__project = ''
        self.__params = ''
        self.__command = ''

    def set_project(self, project):
        self.__project = project

    def set_parameters(self):
        self.__params = JavascriptParameters()
        self.__params.set_language_path(PathCompiler.get_path_compiler(self.__project.language))
        self.__params.set_language_path(JAVASCRIPT14_PATH)
        main_file_path = self.__project.main_file_path
        self.__params.set_file_path(BASE_DIR / main_file_path)

    def build_command(self):
        self.__command = JavascriptBuilderCommand()

    def run(self):
        self.set_parameters()
        self.build_command()
        try:
            process = subprocess.Popen(self.__command.command(self.__params),
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True)
            output, errors = process.communicate()
            return output
        except Exception as err:
            raise ExecuteInvalidException(err)