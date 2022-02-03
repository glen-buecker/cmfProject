from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    cost = models.DecimalField(..., max_digits=6, decimal_places=2)
    active = models.BooleanField

class Organization(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField

class Trip(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField
    description = models.CharField(max_length=300)
    cost = models.DecimalField(..., max_digits=6, decimal_places=2)
    active = models.BooleanField

class Person(models.Model):
    name = models.CharField(max_length=100)
    participation_type = models.CharField(max_length = 25)
    section = models.CharField(max_length = 25)
