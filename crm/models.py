from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(unique=True,max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    publishdate=models.DateField(null=True,blank=True)
    publisher=models.CharField(max_length=200)
    genre=models.CharField(max_length=200,null=True)
    about=models.CharField(max_length=500,null=True)
    picture=models.ImageField(upload_to="images",null=True)