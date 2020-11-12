#
# @model_files.py Copyright (c) 2020 Jalasoft.
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
from code_editor.model_projects import Projects

#Create class to set a new 'Table'
class Files(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    path=models.FileField(upload_to='files/')
    project=models.ForeignKey(Projects, on_delete=models.CASCADE)
    date=models.DateField()
