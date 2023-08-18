from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
    image = models.FilePathField(path="/img")
       
    
