from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    title= models.CharField(max_length=200, null=True)
    Author= models.CharField(max_length=200, null=True)
    Price= models.IntegerField()
    Edition=models.integeField()