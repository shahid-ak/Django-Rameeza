from django.db import models

# Create your models here.

class lenders(models.Model):
    name = models.CharField(max_length=150)
    usn = models.CharField(max_length=150)
    branch = models.CharField(max_length=150)
    authid = models.IntegerField()

class catagories(models.Model):
    name = models.CharField(max_length=150)
    count = models.IntegerField(default=0)

class books(models.Model):
    bookname = models.CharField(max_length=150)
    discription = models.TextField()
    author = models.CharField(max_length=150)
    catagory = models.CharField(max_length=150)
    img=models.ImageField(upload_to='book')

