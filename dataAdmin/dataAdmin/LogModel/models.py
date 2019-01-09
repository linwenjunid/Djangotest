from django.db import models

# Create your models here.
from django.db import models


class Logs(models.Model):
    IP = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    time = models.DateField(auto_now=True)
    operate = models.CharField(max_length=200)