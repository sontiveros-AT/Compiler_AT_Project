#
# @main.py Copyright (c) 2020 Jalasoft.
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

from java_compiler.javacompiler import CompileJava
from java_compiler.parameters_java import ParametersJava


# Setup java version and project's files paths
para = ParametersJava()
# Setup the version el JDK java
para.set_version(13)
# Set up the binaries location 
para.set_binary ('../../media/java/java_files/p2/bin')
# Set up the package classes location
para.set_package('../../media/java/java_files/p2/src/com/*.java')
# Set up the Main Class
para.set_main_app('com.Main')

# Create an CompileJava instance with ParametersJava
proc = CompileJava(para)
# Executed
print(proc.execute_java())
