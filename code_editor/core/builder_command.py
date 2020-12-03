#
# @builder_command.py Copyright (c) 2020 Jalasoft.
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
# Author: Juan S. Ontiveros
# Version: 1.0
#

import subprocess
from abc import ABC, abstractmethod


# Super class that defines the signature to build a command
# based on a specific Parameters class instance
class BuilderCommand(ABC):
    @abstractmethod
    def command(self, params):
        pass
