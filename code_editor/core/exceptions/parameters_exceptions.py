#
# @parameters_exceptions.py Copyright (c) 2020 Jalasoft.
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
# Author: Alvaro Cruz
# Version: 1.0
#

from code_editor.core.exceptions.exceptions import ParametersInvalidException


# Create classes for parameters exceptions

class NoneParametersException(ParametersInvalidException):

    def __str__(self):
        return f'None Parameters Error: {self._desc} {type(self._obj)} {self._obj}'


class EmptyParametersException(ParametersInvalidException):

    def __str__(self):
        return f'Empty Parameters Error: {self._desc} {type(self._obj)} {self._obj}'


class NotFoundParametersException(ParametersInvalidException):

    def __str__(self):
        return f'Not Found Parameters Error: {self._desc}  {self._obj}'
