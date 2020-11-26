#
# @orm_project.py Copyright (c) 2020 Jalasoft.
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

from datetime import datetime
from code_editor.models.model_file import File
from code_editor.models.model_project import Project
from code_editor.models.model_language import Language
from code_editor.orm_queries.orm_file import OrmFile


# OrmProject Class provide the different queries to the DB related with Projects
class OrmProject:
    # Returns an integer with the number of project for a given user (logged in)
    @staticmethod
    def count_all_projects(user):
        return Project.objects.filter(user=user).count()

    # Returns a list of all project for a given user (logged in)
    @staticmethod
    def get_all_projects(user):
        return Project.objects.filter(user=user)

    # Returns a Project Object that belongs to the id_project
    @staticmethod
    def get_project(id_project):
        return Project.objects.get(id_project=id_project)

    # Returns a Language Object that belongs to the id_project
    @staticmethod
    def get_language_project(id_project):
        return Project.objects.get(id_project=id_project).language

    # Returns an integer with the number of files of the id_project
    @staticmethod
    def count_all_files(id_project):
        return File.objects.filter(project_id=id_project).count()

    # Returns an List of all files of the id_project
    @staticmethod
    def get_all_files(id_project):
        return File.objects.filter(project_id=id_project)

    # Updates the main File Object that belongs to the id_project
    @staticmethod
    def update_main_file(id_project, main_file_path):
        project = Project.objects.get(id_project=id_project)
        project.main_file_path = main_file_path
        project.save()

    # Returns the main File Object that belongs to the id_project
    @staticmethod
    def get_main_file(id_project):
        return Project.objects.get(id_project=id_project).main_file_path

    # CREATE A NEW PROJECT
    # Creates a new project on the DB with the project_name, project_description and language
    @staticmethod
    def create_project(name_project, description, project_path, language, user):
        project = Project()
        project.project_name = name_project
        project.project_description = description
        project.project_path = project_path
        lang = Language.objects.get(language_name=language.lower())
        project.language = lang
        project.user = user
        project.save()

        return project

    # DELETE A PROJECT
    # Deletes a project on the DB with the id_project
    @staticmethod
    def delete_project(id_project):
        Project.objects.get(id_project=id_project).delete()
