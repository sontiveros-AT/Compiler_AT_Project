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

from django import forms


class FileForm(forms.Form):
    LANGUAGES = (('py', 'Python'), ('java', 'Java'))

    file_name = forms.CharField(max_length=100)
    description = forms.CharField()
    program = forms.CharField(widget=forms.Textarea)
    language = forms.ChoiceField(choices=LANGUAGES)
