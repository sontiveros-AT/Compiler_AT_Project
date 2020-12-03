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


# OrmFile Class provide the different queries to the DB related with Files
class OrmFile:
    # Returns a File Object with the name_file requested and id_project
    @staticmethod
    def get_file(file_id):
        return File.objects.get(id=file_id)

    # Returns a Language Object with the name_file requested and id_project
    @staticmethod
    def get_language_file(file_id):
        return OrmFile.get_file(file_id).project.language

    # CREATE A NEW FILE
    # Creates a new file on the DB with the id_project and file_name
    @staticmethod
    def create_file(name, file_path, project_id):
        project = Project.objects.get(id=project_id)
        file = File(
            name=name,
            path=file_path,
            creation_date=datetime.now(),
            project=project,
            user=project.user)
        file.save()

        return file

    # UPDATE A FILE
    # Updates a file on the DB with the id_file
    @ staticmethod
    def update_file_name(file_id, new_name):
        File.objects.filter(id=file_id).update(file_name=new_name)

    # DELETE A FILE
    # Deletes a file on the DB with the id_file
    @ staticmethod
    def delete_file(file_id):
        OrmFile.get_file(file_id).delete()
