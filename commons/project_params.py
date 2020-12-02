#
# @project_params.py Copyright (c) 2020 Jalasoft.
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
# Author: Juan Sebastián Ontiveros Gonzales
# Version: 1.0
#

from pathlib import Path
from code_editor.orm_queries.orm_language import OrmLanguage
from code_editor.orm_queries.orm_project import OrmProject
from commons.settings import PYTHON2_HELLO_WORLD
from commons.settings import PYTHON3_HELLO_WORLD
from commons.settings import JAVA13_HELLO_WORLD


class ProjectParameters():

    def __init__(self, project_id):
        self.project = OrmProject.get_project(project_id)
        self.language = self.project.language
        self.language_name = self.language.name.lower()

    def get_main_file_name(self):
        file_name = ''

        if self.language_name == 'java':
            file_name = 'Main'
        else:
            file_name = 'main'

        return Path(f'{file_name}{self.language.extension}')

    def get_hello_world_code(self):
        hello_world_code = ''

        if self.language_name == 'python':
            if self.language.version[0] == '2':
                hello_world_code = PYTHON2_HELLO_WORLD
            if self.language.version[0] == '3':
                hello_world_code = PYTHON3_HELLO_WORLD

        if self.language_name == 'java':
            hello_world_code = JAVA13_HELLO_WORLD

        return hello_world_code

    def get_main_path(self):
        file_path = Path()

        if self.language_name == 'java':
            file_path = Path(self.project.path) / 'src/com'
        else:
            file_path = Path(self.project.path)

        return file_path

    def get_file_name_with_ext(self, file_name):
        extension = '.' + file_name.split('.')[-1]

        if extension == self.language.extension:
            return file_name

        return file_name + self.language.extension
