#
# @javacompiler.py Copyright (c) 2020 Jalasoft.
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


# class compiler built, based in params class
class Compiler:
    def __init__(self, params):
        self.__path_language = params.get_language()
        self.__file = params.get_file()

    # execute the compiler based in the params of the constructor
    def execute(self):
        """execute() -> output of the user file"""
        output = subprocess.run([self.__path_language, self.__file],
                                capture_output=True,
                                text=True)
        print(output.stdout)
        if output.returncode != 0:
            return output.stderr
        return output.stdout

