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
from code_editor.core.settings import BASE_DIR, PYTHON39_HELLO_WORLD, JAVA13_HELLO_WORLD, JAVASCRIPT14_HELLO_WORLD


# class file manager to modify local files


class FileManager:

    # create a file in the media directory based in the language
    def create_file(self, file_name, project_id):
        project = OrmProject.get_project(project_id)
        language = project.language.language_name
        language_id = project.language.id_language
        extension = OrmLanguage.get_extension(language_id)
        file = file_name + extension
        file_path = ''

        if language == 'python':
            file_path = project.project_path
            program = PYTHON39_HELLO_WORLD

        if language == 'java':
            file_path = f'{project.project_path}/src/com'
            program = JAVA13_HELLO_WORLD

        if language == 'javascript':
            file_path = project.project_path
            program = JAVASCRIPT14_HELLO_WORLD

        full_path = BASE_DIR / file_path / file

        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(program)

        OrmFile.create_file(file_name, file_path, project_id)

        return f'{file_path}/{file}'

    # returns the content of the file targeted
    def load_file(self, filepath):
        file = open(filepath, "r")
        program = file.read()
        file.close()
        return program

    # overwrite the targeted file with new text
    def update_file(self, filepath, program):
        file = open(filepath, "w")
        program = file.write(program)
        file.close()

    # remove the targeted file
    def remove_file(self, filepath):
        file_to_rem = Path(filepath)
        file_to_rem.unlink()
