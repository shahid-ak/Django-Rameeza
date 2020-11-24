from django.db import models

# Create your models here.

class lenders(models.Model):
    name = models.CharField(max_length=150)
    usn = models.CharField(max_length=150)
    branch = models.CharField(max_length=150)
    authid = models.IntegerField()

