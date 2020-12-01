#
# @orm_file.py Copyright (c) 2020 Jalasoft.
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


# OrmFile Class provide the different queries to the DB related with Files
class OrmFile:
    # Returns a File Object with the name_file requested and id_project
    @staticmethod
    def get_file(id_file):
        return File.objects.get(id_file=id_file)

    # Returns a Language Object with the name_file requested and id_project
    @staticmethod
    def get_language_file(name_file, id_project):
        lang_id = File.objects.get(file_name=name_file,
                                   project_id=id_project).project_id
        return Language.objects.get(id_language=lang_id)

    # CREATE A NEW FILE
    # Creates a new file on the DB with the id_project and file_name
    @staticmethod
    def create_file(name, file_path, id_project):
        file = File()
        file.file_name = name
        file.file_path = file_path
        file.file_date = datetime.now()
        project = Project.objects.get(id_project=id_project)
        file.project = project
        file.user = project.user
        file.save()

        return file

    # UPDATE A FILE
    # Updates a file on the DB with the id_file
    @staticmethod
    def update_file_name(id_file, new_name):
        File.objects.filter(id_file=id_file).update(file_name=new_name)

    # DELETE A FILE
    # Deletes a file on the DB with the id_file
    @staticmethod
    def delete_file(id_file):
        File.objects.get(id_file=id_file).delete()
