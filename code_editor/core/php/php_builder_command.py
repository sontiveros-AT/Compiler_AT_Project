#
# @php_builder_command.py Copyright (c) 2020 Jalasoft.
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

import subprocess
from code_editor.core.builder_command import BuilderCommand
from code_editor.core.exceptions.command_exceptions import *
from code_editor.core.php.php_parameters import PhpParameters


# class compiler built, based in params class
class PhpBuilderCommand(BuilderCommand):
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
        elif not isinstance(params, PhpParameters):
            raise TypeCommandException(params)
        else:
            return True
