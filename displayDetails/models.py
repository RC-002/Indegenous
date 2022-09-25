from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Info(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    details = models.TextField(null=False)

    def __str__(self):
        return self.title   