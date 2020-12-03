#
# @language_exceptions.py Copyright (c) 2020 Jalasoft.
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

from code_editor.core.exceptions.exceptions import LanguageInvalidException


# Create classes for languages exceptions

class NoneLanguageException(LanguageInvalidException):

    def __str__(self):
        return f'None Language Error: {type(self._lang)}'


class TypeLanguageException(LanguageInvalidException):

    def __str__(self):
        return f'Type Language Error: {type(self._lang)} {self._lang}'


class FoundLanguageException(LanguageInvalidException):

    def __str__(self):
        return f'No Language Found Error: {self._lang}'
