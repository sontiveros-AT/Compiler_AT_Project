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
from code_editor.models.model_language import Language


# OrmLanguage Class provide the different queries to the DB related with Languages
class OrmLanguage:
    # Returns an integer with the number of languages
    @staticmethod
    def count_all_language():
        return len(Language.objects.all())

    # Returns a list of all languages
    @staticmethod
    def get_languages():
        return Language.objects.all()

    # Returns a Language Object with the id_language
    @staticmethod
    def get_language(language_id):
        return Language.objects.get(id=language_id)

    # CREATE A NEW LANGUAGE IN THE DATA BASE
    @staticmethod
    def create_new_language(language_name, language_version, language_extension):
        lang = Language(name=language_name,
                        version=language_version,
                        extension=language_extension)
        lang.save()

    # UPDATE A LANGUAGE IN THE DATA BASE
    @staticmethod
    def update_language(language_id, language_name, language_version, language_extension):
        Language.objects.filter(id=language_id).update(
            name=language_name,
            version=language_version,
            extension=language_extension)

    # DELETE A LANGUAGE IN THE DATA BASE
    @staticmethod
    def delete_language(language_id):
        OrmLanguage.get_language(language_id).delete()

    # GET EXTENSION SUPORTED BY LANGUAGE
    @staticmethod
    def get_extension(language_id):
        return OrmLanguage.get_language(language_id).language_extension

    @staticmethod
    def get_languages_labels():
        lang_list = OrmLanguage.get_languages()
        lang_label = []
        for lang in lang_list:
            if lang.name.capitalize() not in lang_label:
                lang_label.append(lang.name.capitalize())

        total = []
        for la in lang_label:
            partial = []
            aux = []
            for lang in lang_list:
                if la == lang.name.capitalize():
                    n = lang.name.capitalize() + ' ' + lang.version
                    x = [lang.id, n]
                    partial.append(x)
            aux.append(partial)
            aux.insert(0, la)
            total.append(aux)
        return total
