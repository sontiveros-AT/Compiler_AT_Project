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

import os.path
import subprocess

from subprocess import STDOUT, PIPE

class CompileJava:
    def __init__(self, para):
        self.__path = para.get_version()   
        self.__binary = para.get_binary()
        self.__package = para.get_package()
        self.__mainapp = para.get_main_app()

    # Executes the java compiler and Runs the Main class
    def execute_java (self):
        cmd=[self.__path+"\javac", "-d" , self.__binary ,self.__package, "&&", self.__path+"\java", "-cp", self.__binary, self.__mainapp]
        proc=subprocess.Popen(cmd, stdout = PIPE, stderr = STDOUT, shell=True)
        output = proc.stdout.read().decode('utf-8')
        return output
		