#
# @python_executor.py Copyright (c) 2020 Jalasoft.
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

from code_editor.core.exceptions.exceptions import ExecuteInvalidException
from code_editor.core.executor import Executor


# Class to execute Python commands

class PythonExecutor(Executor):
    def run(self, cmd):
        try:
            output = subprocess.run(cmd, capture_output=True, text=True)
            if output.returncode != 0:
                return output.stderr
            return output.stdout
        except ExecuteInvalidException as e:
            pass
