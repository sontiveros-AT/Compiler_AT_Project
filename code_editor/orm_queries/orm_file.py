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
    def get_file(name_file, id_project):
        return File.objects.get(file_name=name_file, project_id=id_project)

    # Returns a File Object with the name_file requested and id_project
    @staticmethod
    def get_language_file(name_file, id_project):
        id = File.objects.get(file_name=name_file, project_id=id_project).project_id
        return Language.objects.get(id_language=id)

    # CREATE A NEW FILE
    # Creates a new file on the DB with the id_project and file_name
    @staticmethod
    def create_file(id_project, name):
        pro = Project.objects.get(id_project=id_project)
        lang = Language.objects.get(id_language=pro.language_id)
        file = File()
        file.file_name = name
        if lang.language_name == 'java':
            file.file_path = pro.project_path + '/src/com/' + name + lang.language_extension
        elif lang.language_name == 'python':
            file.file_path = pro.project_path + '/' + name.lower() + lang.language_extension
        file.file_date = datetime.now()
        file.project = pro
        file.save()

    # UPDATE A FILE
    # Updates a file on the DB with the id_file
    @staticmethod
    def update_file_name(id_file, new_name):
        file = File.objects.get(id_file=id_file)
        pro = Project.objects.get(id_project=file.project_id)
        lang = Language.objects.get(id_language=pro.language_id)
        File.objects.filter(id_file=id_file).update(file_name=new_name)
        File.objects.filter(id_file=id_file).update(file_path=pro.project_path+'/'+new_name+lang.language_extension)

    # DELETE A FILE
    # Deletes a file on the DB with the id_file
    @staticmethod
    def delete_file(id_file):
        File.objects.get(id_file=id_file).delete()
