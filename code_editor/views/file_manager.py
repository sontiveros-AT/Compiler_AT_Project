#
# @file_manager.py Copyright (c) 2020 Jalasoft.
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
# Author: Andres Cox
# Version: 1.0

import os
from pathlib import Path
from code_editor.orm_queries.orm_file import OrmFile
from code_editor.orm_queries.orm_language import OrmLanguage
from code_editor.orm_queries.orm_project import OrmProject
from code_editor.core.settings import BASE_DIR, PYTHON39_HELLO_WORLD, JAVA13_HELLO_WORLD

# class file manager to modify local files


class FileManager:

    # create a file in the media directory based in the language
    def create_file(self, project_id, file_name, path=''):
        file_path, program = self.get_file_data(
            project_id, file_name, path='')
        full_path = BASE_DIR / file_path
        file_name = full_path.name

        file = OrmFile.create_file(file_name, file_path, project_id)

        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        self.update_file(file.id_file, program)

        return file_path

    def get_file_data(self, project_id, file_name, path=''):
        project = OrmProject.get_project(project_id)
        language = project.language.language_name
        extension = OrmLanguage.get_extension(language)
        file = file_name + extension

        if language == 'python':
            file_path = f'{project.project_path}/{path}'
            program = PYTHON39_HELLO_WORLD

        if language == 'java':
            file_path = f'{project.project_path}/src/com/{path}'
            program = JAVA13_HELLO_WORLD

        return (f'{file_path}/{file}', program)

    # returns the content of the file targeted
    def load_file(self, file_id):
        full_path = BASE_DIR / OrmFile.get_file(file_id).file_path

        with open(full_path, "r") as file:
            program = file.read()

        return program

    # overwrite the targeted file with new text
    def update_file(self, file_id, program):
        full_path = BASE_DIR / OrmFile.get_file(file_id).file_path

        with open(full_path, "w") as file:
            file.write(program)

    # remove the targeted file
    def remove_file(self, file_id):
        full_path = BASE_DIR / OrmFile.get_file(file_id).file_path

        file_to_rem = Path(full_path)
        file_to_rem.unlink()
        OrmFile.delete_file(file_id)
