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

import os
from code_editor.core.parameters import Parameters
from code_editor.core.exceptions.parameters_exceptions import *


# class parameters to establish user_file and binaries location
class PythonParameters(Parameters):
    def __init__(self):
        super().__init__()

    def validate(self):
        if self.get_file_path() is None:
            raise NoneParametersException(self.get_file_path(), 'file path')
        elif self.get_language_path() is None:
            raise NoneParametersException(self.get_language_path(), 'language path')
        elif self.get_file_path() == '':
            raise EmptyParametersException(self.get_file_path(), 'file path')
        elif self.get_language_path() == '':
            raise EmptyParametersException(self.get_language_path(), 'file language')
        elif not os.path.isfile(self.get_file_path()):
            raise NotFoundParametersException(self.get_file_path(), 'file path')
        elif not os.path.isfile(self.get_language_path()):
            raise NotFoundParametersException(self.get_language_path(), 'file language')