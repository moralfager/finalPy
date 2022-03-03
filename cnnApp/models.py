from operator import mod
from django.db import models

# Create your models here.

class Image(models.Model):
    name=models.TextField()
    link=models.TextField()
    