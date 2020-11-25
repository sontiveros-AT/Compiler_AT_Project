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
from code_editor.core.settings import PYTHON39_PATH, PYTHON_PROJECTS
from code_editor.core.python.python_builder_command import PythonBuilderCommand
from code_editor.core.python.python_parameters import PythonParameters


# Class to execute Python commands
class PythonExecutor(Executor):
  
    def __init__(self):
        self.__project_name = ''
        self.__params = ''
        self.__command = ''
        self.__executor = ''

    def set_project_name(self, project_name):
        self.__project_name = project_name

    def set_parameters(self):
        self.__params = PythonParameters()
        self.__params.set_language_path(PYTHON39_PATH)
        self.__params.set_file_path(PYTHON_PROJECTS / f'{self.__project_name}/main.py')

    def build_command(self):
        self.__command = PythonBuilderCommand()

    def run(self):
        self.set_parameters()
        self.build_command()
        process = subprocess.Popen(self.__command.command(self.__params),
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True)
        output, errors = process.communicate()
        return output
