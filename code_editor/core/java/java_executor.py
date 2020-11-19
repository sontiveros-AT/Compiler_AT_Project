#
# @java_executor.py Copyright (c) 2020 Jalasoft.
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
from subprocess import STDOUT, PIPE
from code_editor.core.executor import Executor

# Class executor using popen

class JavaExecutor(Executor):
    def run(self, cmd):
        proc = subprocess.Popen(cmd, stdout=PIPE,
                                stderr=STDOUT, shell=True)
        output = proc.stdout.read().decode('utf-8')
        return output
