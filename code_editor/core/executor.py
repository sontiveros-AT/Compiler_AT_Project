#
# @executor.py Copyright (c) 2020 Jalasoft.
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

# Super class that defines the signature
# to run a command to compile a file


class Executor(ABC):

    @abstractmethod
    def set_project_name(self, project_name):
        pass

    @abstractmethod
    def set_parameters(self):
        pass

    @abstractmethod
    def build_command(self):
        pass

    @abstractmethod
    def run(self):
        pass
