from django.db import models

# Create your models here.

class user(models.Model):
    firstname = models.CharField(max_length=20,default='')
    lastname = models.CharField(max_length=20,default='')
    email = models.CharField(max_length=20,default='')
    username = models.CharField(max_length=20,default='')
    upass = models.CharField(max_length=20,default='')