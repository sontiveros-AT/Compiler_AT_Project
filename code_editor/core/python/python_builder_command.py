#
# @python_builder_command.py Copyright (c) 2020 Jalasoft.
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

import subprocess
from code_editor.core.builder_command import BuilderCommand
from code_editor.core.exceptions.command_exceptions import *
from code_editor.core.python.python_parameters import PythonParameters


# Class compiler built, based in params class
class PythonBuilderCommand(BuilderCommand):
    def command(self, params):
        self.validate(params)
        cmd = params
        language_path = cmd.get_language_path()
        file_path = cmd.get_file_path()

        return [language_path, file_path]

    def validate(self, params):
        if params is None:
            raise NoneCommandException(params)
        elif params == '':
            raise EmptyCommandException(params)
        elif not isinstance(params, PythonParameters):
            raise TypeCommandException(params)
        else:
            return True
