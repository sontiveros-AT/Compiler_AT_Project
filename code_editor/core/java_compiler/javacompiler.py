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


def compile_java (java_file):
    proc_compiler=subprocess.Popen(['javac', '-d' ,'bin' ,java_file], stdout = PIPE, stderr = STDOUT)
    compiler_output = proc_compiler.stdout.read().decode('utf-8')
    print(compiler_output)

def execute_java (java_file):
    cmd=['java', '-cp', 'bin', java_file]
    proc=subprocess.Popen(cmd, stdout = PIPE, stderr = STDOUT)
    output = proc.stdout.read().decode('utf-8')
    print(output)
    
compile_java("src/com/*.java")
execute_java("com.GreetingApp")
