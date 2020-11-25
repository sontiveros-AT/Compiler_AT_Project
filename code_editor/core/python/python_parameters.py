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
from abc import ABC

from code_editor.core.exceptions.exceptions import ParametersInvalidException
from code_editor.core.parameters import Parameters


# class parameters to establish user_file and binaries location
class PythonParameters(Parameters):
    def __init__(self):
        super().__init__()

    def validate(self):
        #self.set_file('/media/python/sdasdasd')
        file_path = self.get_file()
        language_path = self.get_language()
        if os.path.isfile(file_path) and os.path.isfile(language_path):
            print('Todo Ok')
        else:
            raise ParametersInvalidException
            print('No existe')

