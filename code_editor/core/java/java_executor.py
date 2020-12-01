#
# @java_executor.py Copyright (c) 2020 Jalasoft.
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
from code_editor.core.exceptions.exceptions import ExecuteInvalidException
from code_editor.core.settings import JAVA13_PATH, BASE_DIR

import subprocess
from subprocess import STDOUT, PIPE
from code_editor.core.executor import Executor
from code_editor.core.java.java_builder_command import JavaBuilderCommand
from code_editor.core.java.java_parameters import JavaParameters


# Class executor for java
class JavaExecutor(Executor):
    def __init__(self):
        self.__project = ''
        self.__params = ''
        self.__command = ''

    def set_project(self, project):
        self.__project = project

    def set_version(self, version):
        self.__version = version

    def set_parameters(self):
        self.__params = JavaParameters()
        self.__params.set_language_path(JAVA13_PATH)
        project_path = self.__project.project_path
        self.__params.set_binary(BASE_DIR / project_path / 'bin')
        self.__params.set_package(BASE_DIR / project_path / 'src/com/*.java')
        self.__params.set_file_path('com.Main')
        self.__params.validate()

    def build_command(self):
        self.__command = JavaBuilderCommand()

    def run(self):
        self.set_parameters()
        self.build_command()

        try:
            proc = subprocess.Popen(self.__command.command(self.__params), stdout=PIPE,
                                stderr=STDOUT, shell=True)
            output = proc.stdout.read().decode('utf-8')
            return output
        except Exception as err:
            raise ExecuteInvalidException(err)
