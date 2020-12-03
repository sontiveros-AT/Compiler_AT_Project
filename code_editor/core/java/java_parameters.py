#
# @java_parameters.py Copyright (c) 2020 Jalasoft.
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
# Author: Alvaro Cruz, Juan S. Ontiveros
# Version: 1.0
#


import os
from code_editor.core.exceptions.parameters_exceptions import *
from code_editor.core.parameters import Parameters


# Class to define getter and setter (binarys & packages)
class JavaParameters(Parameters):
    def __init__(self):
        super().__init__()
        self.__binary = ''
        self.__package = ''

    # Getter Setter Binary
    def get_binary(self):
        return self.__binary

    def set_binary(self, binary):
        self.__binary = binary

    # Getter Setter Package
    def get_package(self):
        return self.__package

    def set_package(self, package):
        self.__package = package

    def validate(self):

        if self.get_file_path() is None:
            raise NoneParametersException(self.get_file_path(), 'file path')
        elif self.get_language_path() is None:
            raise NoneParametersException(self.get_language_path(), 'language path')
        elif self.get_binary() is None:
            raise NoneParametersException(self.get_binary(), 'binary path')
        elif self.get_package() is None:
            raise NoneParametersException(self.get_package(), 'package path')
        elif self.get_file_path() == '':
            raise EmptyParametersException(self.get_file_path(), 'file path')
        elif self.get_language_path() == '':
            raise EmptyParametersException(self.get_language_path(), 'file language')
        elif self.get_binary() == '':
            raise EmptyParametersException(self.get_binary(), 'binary path')
        elif self.get_package() == '':
            raise EmptyParametersException(self.get_package(), 'package path')
