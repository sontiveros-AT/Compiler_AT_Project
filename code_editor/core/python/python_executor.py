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
from code_editor.core.executor import Executor
from commons.settings import PYTHON39_PATH, BASE_DIR
from code_editor.core.python.python_builder_command import PythonBuilderCommand
from code_editor.core.python.python_parameters import PythonParameters


# Class to execute Python commands
class PythonExecutor(Executor):

    def __init__(self):
        self.__file = ''
        self.__project = ''
        self.__params = ''
        self.__command = ''

    def set_file(self, file):
        self.__file = file

    def set_parameters(self):
        self.__params = PythonParameters()
        self.__params.set_language_path(PYTHON39_PATH)
        self.__params.set_file_path(BASE_DIR / self.__file.path)

    def build_command(self):
        self.__command = PythonBuilderCommand()

    def run(self):
        self.set_parameters()
        self.build_command()
        process = subprocess.Popen(self.__command.command(self.__params),
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True)
        output, err = process.communicate()

        return output if output else err
