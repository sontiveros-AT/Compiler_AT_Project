#
# @path_compiler.py Copyright (c) 2020 Jalasoft.
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

from commons.settings import PYTHON39_PATH, PYTHON27_PATH, JAVA13_PATH, JAVASCRIPT14_PATH


class PathCompiler:

    @staticmethod
    def get_path_compiler(language):

        if language.name == 'python':
            if language.version == '3.9':
                return PYTHON39_PATH
            elif language.version == '2.7':
                return PYTHON27_PATH

        elif language.name == 'java':
            if language.version == '13.0.2':
                return JAVA13_PATH

        elif language.name == 'javascript':
            if language.version == '14.15.1':
                return JAVASCRIPT14_PATH
