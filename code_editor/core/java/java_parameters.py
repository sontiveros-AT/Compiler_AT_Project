#
# @parameters_java.py Copyright (c) 2020 Jalasoft.
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

# All java jdk must be directed here
# This path should be changed pointing to the java jdk folder.

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
