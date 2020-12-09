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

from accounts.models import UserProfile
from code_editor.models.model_file import File
from code_editor.models.model_project import Project
from code_editor.orm_queries.orm_file import OrmFile
from code_editor.orm_queries.orm_language import OrmLanguage
from accounts.orm_queries.orm_user import OrmUser


# OrmProject Class provide the different queries to the DB related with Projects
class OrmProject:
    # Returns an integer with the number of project for a given user (logged in)
    @staticmethod
    def count_all_projects(user):
        return OrmProject.get_all_projects(user).count()

    # Returns a list of all project for a given user (logged in)
    @staticmethod
    def get_all_projects(user):
        return Project.objects.filter(user=user)

    # Returns a Project Object that belongs to the id_project
    @staticmethod
    def get_project(project_id):
        return Project.objects.get(id=project_id)

    # Returns a Language Object that belongs to the id_project
    @staticmethod
    def get_language_project(project_id):
        return OrmProject.get_project(project_id).language

    # Returns an integer with the number of files of the id_project
    @staticmethod
    def count_all_files(project_id):
        return OrmProject.get_all_files(project_id).count()

    # Returns an List of all files of the id_project
    @staticmethod
    def get_all_files(project_id):
        project = OrmProject.get_project(project_id)
        user = project.user
        return File.objects.filter(project=project, user=user)

    # Returns the main File Object that belongs to the id_project
    @staticmethod
    def get_main_file(project_id):
        files = OrmProject.get_all_files(project_id)
        for file in files:
            if file.is_main:
                return file

    # CREATE A NEW PROJECT
    # Creates a new project on the DB with the project_name, project_description and language
    @staticmethod
    def create_project(name_project, description, project_path, language_id, user_id):
        project = Project(
            name=name_project,
            description=description,
            path=project_path,
            language=OrmLanguage.get_language(language_id),
            user=OrmUser.get_user(user_id))
        project.save()

        return project

    # DELETE A PROJECT
    # Deletes a project on the DB with the id_project
    @staticmethod
    def delete_project(project_id):
        OrmProject.get_project(project_id).delete()

    # @staticmethod
    # def hard_project(project_name, project_description, project_path, main_file_path):
    #     lang = Language.objects.get(id_language=3)
    #     us = UserProfile.objects.get(id=1)
    #     project = Project()
    #     project.project_name = project_name
    #     project.project_description = project_description
    #     project.project_path = project_path
    #     project.main_file_path = main_file_path
    #     project.language = lang
    #     project.user = us
    #     project.save()
