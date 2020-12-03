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
# Author: Gonzalo Alarcon, Alvaro Cruz
# Version: 1.0
#

from django.db import models


# Create class to set a new 'Table'
class Language(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    extension = models.CharField(max_length=30)

    class Meta:
        db_table = 'language'
