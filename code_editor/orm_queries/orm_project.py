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
    # Returns an integer with the number of project
    @staticmethod
    def count_all_projects():
        return Project.objects.all().count()

    # Returns a list of all project
    @staticmethod
    def get_all_projects():
        return Project.objects.all()

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

    # Returns the main File Object that belongs to the id_project
    @staticmethod
    def get_main_file_project(id_project):
        project = Project.objects.get(id_project=id_project)
        print(project.project_name)
        lang = Language.objects.get(id_language=project.language_id)
        if lang.language_name == 'java':
            return File.objects.get(project_id=id_project, file_name='Main')
        elif lang.language_name == 'python':
            return File.objects.get(project_id=id_project, file_name='main')

    # CREATE A NEW PROJECT
    # Creates a new project on the DB with the project_name, project_description and language
    @staticmethod
    def create_project(name, description, language):
        project = Project()
        project.project_name = name
        project.project_description = description
        lang = Language.objects.get(language_name=language.lower())
        project.language = lang
        if lang.language_name == 'java':
            project.project_path = '/media/java/' + name
        elif lang.language_name == 'python':
            project.project_path = '/media/python/' + name
        project.save()

    # DELETE A PROJECT
    # Deletes a project on the DB with the id_project
    @staticmethod
    def delete_project(id_project):
        Project.objects.get(id_project=id_project).delete()

    # INTEGRATED END POINT
    # CREATE A NEW PROJECT WITH A MAIN FILE ON IT

    @staticmethod
    def create_simple_project(name_project, description, language):
        project = Project()
        project.project_name = name_project
        project.project_description = description
        lang = Language.objects.get(language_name=language.lower())
        project.language = lang
        if lang.language_name == 'java':
            project.project_path = '/media/java/' + name_project
        elif lang.language_name == 'python':
            project.project_path = '/media/python/' + name_project
        project.save()
        MAIN_NAME = 'Main'
        OrmFile.create_file(project.id_project, MAIN_NAME)

        return project
