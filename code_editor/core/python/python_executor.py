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

import subprocess

from code_editor.core.exceptions.exceptions import ExecuteInvalidException
from code_editor.core.executor import Executor
from code_editor.core.settings import PYTHON39_PATH, BASE_DIR, PYTHON27_PATH
from code_editor.core.python.python_builder_command import PythonBuilderCommand
from code_editor.core.python.python_parameters import PythonParameters


# Class to execute Python commands
class PythonExecutor(Executor):

    def __init__(self):
        self.__project = ''
        self.__params = ''
        self.__command = ''

    def set_project(self, project):
        self.__project = project

    def set_version(self, version):
        self.__version = version

    def set_parameters(self):
        self.__params = PythonParameters()
        if self.__version == '3.9':
            self.__params.set_language_path(PYTHON39_PATH)
        elif self.__version == '2.7':
            self.__params.set_language_path(PYTHON27_PATH)
        main_file_path = self.__project.main_file_path
        self.__params.set_file_path(BASE_DIR / main_file_path)
        #self.__params.validate()

    def build_command(self):
        self.__command = PythonBuilderCommand()

    def run(self):
        self.set_parameters()
        self.build_command()
        #try:
        process = subprocess.Popen(self.__command.command(self.__params),
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True)
        output, errors = process.communicate()
        return output
        #except Exception as err:
            #raise ExecuteInvalidException(err)
