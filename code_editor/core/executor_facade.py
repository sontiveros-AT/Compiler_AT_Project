#
# @executor_facade.py Copyright (c) 2020 Jalasoft.
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

from code_editor.core.python.python_executor import PythonExecutor
from code_editor.core.java.java_executor import JavaExecutor


# To manage Java and Python parameters and commands
class CompilerFactory:

    def create_compiler(self, language):
        executor_class = language.capitalize() + "Executor"
        return globals()[executor_class]()
