#
# @model_file.py Copyright (c) 2020 Jalasoft.
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
from code_editor.models.model_project import Project


# Create class to set a new 'Table'
class File(models.Model):
    id_file = models.AutoField(primary_key=True, unique=True)
    file_name = models.CharField(max_length=50, null=False, blank=False)
    file_path = models.CharField(max_length=150, null=False, blank=False)
    file_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = 'file'
