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
from accounts.orm_queries.orm_user import OrmUser
from commons.project_params import ProjectParameters
from commons.settings import BASE_DIR

# class file manager to modify local files


class FileManager:

    @staticmethod
    def is_repeated_project(project_name, language_id, user_id):
        user = OrmUser.get_user(user_id)
        for project in OrmProject.get_all_projects(user):
            print(project.name)
            print(type(project.language.id), type(language_id))
            print(project.language.id == language_id)
            if (project.language.id == language_id) and (project.name == project_name):
                return True
        return False

    # create a project in the media directory based in the language and user hashed folder
    @staticmethod
    def create_project(project_name, description, language_id, user_id):
        user_dir = OrmUser.get_user_dir(user_id)
        language = OrmLanguage.get_language(language_id)
        project_path = 'media' / Path(user_dir) / language.name / \
            language.version / project_name

        # create project in the database and sends the id
        print(FileManager.is_repeated_project(
            project_name, language_id, user_id))
        if not FileManager.is_repeated_project(project_name, language_id, user_id):
            project = OrmProject.create_project(
                project_name, description, project_path, language_id, user_id)

            # creates file and adds it to the database
            parameters = ProjectParameters(project.id)
            file_name = parameters.get_main_file_name()

            main_file = FileManager.create_file(project.id, file_name)
            main_file.is_main = True
            main_file.save()

            return project

        return None

    # create a file in the media directory based in the language
    @staticmethod
    def create_file(project_id, file_name, path=''):
        parameters = ProjectParameters(project_id)
        main_path = parameters.get_main_path()
        code = parameters.get_hello_world_code()

        file_path = main_path / path / file_name
        full_path = BASE_DIR / file_path
        file = OrmFile.create_file(file_name, file_path, project_id)

        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        FileManager.update_file(file.id, code)

        return file

    # returns the content of the file targeted
    @staticmethod
    def load_file(file_id):
        full_path = BASE_DIR / OrmFile.get_file(file_id).path

        with open(full_path, "r") as file:
            program = file.read()

        return program

    # overwrite the targeted file with new text
    @staticmethod
    def update_file(file_id, program):
        full_path = BASE_DIR / OrmFile.get_file(file_id).path

        with open(full_path, "w") as file:
            file.write(program)

    # remove the targeted file
    @staticmethod
    def remove_file(file_id):
        full_path = BASE_DIR / OrmFile.get_file(file_id).path

        file_to_rem = Path(full_path)
        file_to_rem.unlink()
        OrmFile.delete_file(file_id)
