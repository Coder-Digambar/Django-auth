from django.db import models

# Create your models here.
class stud(models.Model):
    name = models.CharField(max_length=20,default='')
    gender = models.CharField(max_length=20,default='')

    studstatus = models.TextChoices('studstatus','BLOCK UNBLOCK')
    status = models.CharField(max_length=20,default='BLOCK')