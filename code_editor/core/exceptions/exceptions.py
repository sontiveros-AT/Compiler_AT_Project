#
# @exceptions.py Copyright (c) 2020 Jalasoft.
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

class LanguageInvalidException(Exception):
    def __init__(self, lang):
        self._lang = lang

    def __str__(self):
        return f'Language Error: {type(self._lang)}'


class ParametersInvalidException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'Parameters Invalid Error'


class CommandInvalidException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'Command Invalid Error'


class ExecuteInvalidException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'Execute Invalid Error'
