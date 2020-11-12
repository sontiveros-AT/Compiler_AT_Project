from django.db import models
from code_editor.model_projects import Projects


class Files(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    path=models.FileField(upload_to='files/')
    project=models.ForeignKey(Projects, on_delete=models.CASCADE)
    date=models.DateField()