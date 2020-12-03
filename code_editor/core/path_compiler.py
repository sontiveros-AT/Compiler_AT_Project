#
# @path_compiler.py Copyright (c) 2020 Jalasoft.
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

from commons.configuration.config_manager import ConfigManager
from commons.settings import BASE_DIR


# Class that requests and returns the path of a language binary
class PathCompiler:

    @staticmethod
    def get_path_compiler(language):
        con = ConfigManager()
        return BASE_DIR / con.get_path_compiler(str(language.id))
