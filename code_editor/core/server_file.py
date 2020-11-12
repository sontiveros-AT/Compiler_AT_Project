#
# @server_file.py Copyright (c) 2020 Jalasoft.
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

from compile.compiler import Compiler
from compile.parameters import Parameters


# establish file and language for params
params = Parameters()
params.set_language('python')
params.set_file(r'../../media/python/client_files/client_file.py')

# execute file
program = Compiler(params)
program.execute()
