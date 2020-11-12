#
# @parameters.py Copyright (c) 2020 Jalasoft.
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
from django.conf import settings

PYTHON39_PATH = settings.BASE_DIR / r'third_parties\python\Python39-32\python.exe'


# class parameters to establish user_file and binaries location
class Parameters:
    def __init__(self):
        self.__path_language = ''
        self.__file = ''

    def get_language(self):
        return self.__path_language

    def set_language(self, language):
        if language == 'python':
            self.__path_language = PYTHON39_PATH

    def get_file(self):
        return self.__file

    def set_file(self, file):
        self.__file = file
