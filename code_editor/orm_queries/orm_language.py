#
# @orm_language.py Copyright (c) 2020 Jalasoft.
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


# OrmLanguage Class provide the different queries to the DB related with Languages
class OrmLanguage:
    # Returns an integer with the number of languages
    @staticmethod
    def count_all_language():
        return Language.objects.all().count()

    # Returns a list of all languages
    @staticmethod
    def get_languages():
        return Language.objects.all()

    # Returns a Language Object with the id_language
    @staticmethod
    def get_language(id_language):
        return Language.objects.get(id_language=id_language)

    # CREATE A NEW LANGUAGE IN THE DATA BASE
    @staticmethod
    def create_new_language(language_name, language_version, language_extension):
        lang = Language(language_name=language_name,
                        language_version=language_version,
                        language_extension=language_extension)
        lang.save()

    # UPDATE A LANGUAGE IN THE DATA BASE
    @staticmethod
    def update_language(id_language, language_name, language_version, language_extension):
        Language.objects.filter(id_language=id_language).update(
            language_name=language_name, language_version=language_version, language_extension=language_extension)

    # DELETE A LANGUAGE IN THE DATA BASE
    @staticmethod
    def delete_language(id_language):
        Language.objects.get(id_language=id_language).delete()

    # GET EXTENSION SUPORTED BY LANGUAGE
    @staticmethod
    def get_extension(id_language):
        return Language.objects.get(id_language=id_language).language_extension
