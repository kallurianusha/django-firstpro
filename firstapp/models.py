from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname  = models.CharField(max_length=100)
    salary    = models.CharField(max_length=50)
    age       = models.CharField(max_length=50)
    gender    = models.CharField(max_length =500)
    email     = models.CharField(max_length=50)
    domain    = models.CharField(max_length =25)
    company   = models.CharField(max_length=25)
    experience= models.CharField(max_length=25)
    