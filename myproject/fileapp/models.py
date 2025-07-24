from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100,default='')
    author = models.CharField(max_length=100,default='')
    docs = models.FileField(max_length=300,upload_to='book/docs',default='')
    cover = models.ImageField(max_length=300,upload_to='book/cover',default='')