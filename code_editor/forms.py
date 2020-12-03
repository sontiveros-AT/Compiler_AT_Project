#
# @forms.py Copyright (c) 2020 Jalasoft.
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

from django import forms
from code_editor.orm_queries.orm_language import OrmLanguage


# Tuple of (language_id, language_label) for dropdown list


def get_languages_labels():
    lang_list = OrmLanguage.get_languages()
    lang_label = []
    for lang in lang_list:
        if lang.name not in lang_label:
            lang_label.append(lang.name)

    total = []
    for la in lang_label:
        partial = []
        aux = []
        for lang in lang_list:
            if la == lang.name:
                n = lang.name+' '+lang.version
                x = [lang.id, n]
                partial.append(x)
        aux.append(partial)
        aux.insert(0, la)
        total.append(aux)
    return total


# file form to edit in html
class FileForm(forms.Form):
    #program = forms.CharField(widget=forms.Textarea)
    program = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '100', 'rows': '15'}))

# project form to display in html


class ProjectForm(forms.Form):

    if OrmLanguage.count_all_language() == 0:
        LANGUAGES = ''
    else:
        LANGUAGES = get_languages_labels()

    project_name = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': "Enter project name"}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Project Description"}))
    language = forms.ChoiceField(
        choices=LANGUAGES, widget=forms.Select(attrs={'class': 'form-control'}))
