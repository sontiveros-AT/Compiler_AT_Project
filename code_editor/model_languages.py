from django.db import models

class Languages(models.Model):
    id=models.AutoField(primary_key=True)
    languageName=models.CharField(max_length=30)
    extension=models.CharField(max_length=30)