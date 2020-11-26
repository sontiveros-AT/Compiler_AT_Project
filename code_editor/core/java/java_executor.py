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

from code_editor.core.settings import JAVA13_PATH, JAVA_PROJECTS

import subprocess
from subprocess import STDOUT, PIPE
from code_editor.core.executor import Executor
from code_editor.core.java.java_builder_command import JavaBuilderCommand
from code_editor.core.java.java_parameters import JavaParameters


# Class executor
class JavaExecutor(Executor):
    def __init__(self):
        self.__project_name = ''
        self.__params = ''
        self.__command = ''
        self.__executor = ''

    def set_project_name(self, project_name):
        self.__project_name = project_name

    def set_parameters(self):
        self.__params = JavaParameters()
        self.__params.set_language_path(JAVA13_PATH)
        self.__params.set_binary(JAVA_PROJECTS / f'{self.__project_name}/bin')
        self.__params.set_package(JAVA_PROJECTS / f'{self.__project_name}/src/com/*.java')
        self.__params.set_file_path('com.Main')

    def build_command(self):
        self.__command = JavaBuilderCommand()

    def run(self):
        self.set_parameters()
        self.build_command()

        proc = subprocess.Popen(self.__command.command(self.__params), stdout=PIPE,
                                stderr=STDOUT, shell=True)
        output = proc.stdout.read().decode('utf-8')

        return output
