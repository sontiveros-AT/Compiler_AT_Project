from django.db import models
from code_editor.model_languages import Languages


class Projects(models.Model):
    id=models.AutoField(primary_key=True)
    projectName=models.CharField(max_length=100, null=False)
    description=models.TextField()
    directory=models.FileField(upload_to='files/')
    language=models.ForeignKey(Languages, on_delete=models.CASCADE)