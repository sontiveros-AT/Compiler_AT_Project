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

from code_editor.core.settings import PYTHON39_PATH, JAVA13_PATH, JAVA_FILES

from code_editor.core.python.python_builder_command import PythonBuilderCommand
from code_editor.core.python.python_parameters import PythonParameters
from code_editor.core.python.python_executor import PythonExecutor

from code_editor.core.java.java_builder_command import JavaBuilderCommand
from code_editor.core.java.java_parameters import JavaParameters
from code_editor.core.java.java_executor import JavaExecutor


class ExecutorManager:
    def __init__(self, language="python", file=''):
        self.__language = language.lower()
        self.__main_file = file
        self.__params = ''
        self.__command = ''
        self.__executor = ''

    def set_language(self, language):
        self.__language = language.lower()

    def set_file(self, file_path):
        self.__main_file = file_path

    def __set_parameters(self, binary='', package=''):
        if self.__language == "python":
            self.__params = PythonParameters()
            self.__params.set_language(PYTHON39_PATH)
            self.__params.set_file(self.__main_file)

        if self.__language == "java":
            self.__params = JavaParameters()
            self.__params.set_language(JAVA13_PATH)
            self.__params.set_binary(JAVA_FILES / f'{self.__main_file}/bin')
            self.__params.set_package(
                JAVA_FILES / f'{self.__main_file}/src/com/*.java')
            self.__params.set_file('com.Main')

        print("params")
        print(self.__params.get_language())
        print(self.__params.get_file())

    def __build_command(self):
        if self.__language == "python":
            self.__command = PythonBuilderCommand()

        if self.__language == "java":
            self.__command = JavaBuilderCommand()

    def run(self):
        self.__set_parameters()
        self.__build_command()

        if self.__language == "python":
            self.__executor = PythonExecutor()

        if self.__language == "java":
            self.__executor = JavaExecutor()

        print(self.__language)
        print(self.__command)
        print(self.__command.command(self.__params))

        return self.__executor.run(self.__command.command(self.__params))
