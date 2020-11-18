#
# @model_language.py Copyright (c) 2020 Jalasoft.
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

from django.db import models


# Create class to set a new 'Table'
class Language(models.Model):
    id_language = models.AutoField(primary_key=True, unique=True)
    language_name = models.CharField(max_length=30, null=False, blank=False)
    language_extension = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        db_table = 'language'
