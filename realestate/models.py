from django.db import models
import uuid

# Create your models here.

class Users(models.Model):
    user=models.CharField(max_length=200)
    password=models.CharField(max_length=50)


class Sivangangai(models.Model):
    owner=models.CharField(max_length=200)
    date=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    image=models.CharField(max_length=2080)
    address=models.CharField(max_length=2000)
    size=models.IntegerField()   
    are=models.CharField(max_length=2080,default='Sivagangai')

class Thiruvallur(models.Model):
    owner=models.CharField(max_length=200)
    date=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    image=models.CharField(max_length=2080)
    address=models.CharField(max_length=2000)
    are=models.CharField(max_length=2080,default='Thiruvallur')
    size=models.IntegerField()   


class Thanjavur(models.Model):
    owner=models.CharField(max_length=200)
    date=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    image=models.CharField(max_length=2080)
    address=models.CharField(max_length=2000)
    are=models.CharField(max_length=2080,default='Thanjavur')
    size=models.IntegerField()   

class Comments(models.Model):
    name=models.CharField(max_length=250)
    number=models.IntegerField()
    email=models.EmailField()
    comment=models.TextField()


class Contacts(models.Model):
    name=models.CharField(max_length=250)
    number=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()

