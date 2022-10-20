from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=123)
    surname = models.CharField(max_length=123)

class Person1(models.Model):
    name = models.CharField(max_length=123)
    surname = models.CharField(max_length=123)