#
# @code_editor.py Copyright (c) 2020 Jalasoft.
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

# Import other classes to create ForignKeys
from django.db import models
from code_editor.models.model_language import Language
from accounts.models import UserProfile


# Create class to set a new 'Table'
class Project(models.Model):
    id_project = models.AutoField(primary_key=True, unique=True)
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_path = models.CharField(max_length=100)
    main_file_path = models.CharField(max_length=100, default='')
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)

    class Meta:
        db_table = 'project'
