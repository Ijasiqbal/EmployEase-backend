from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    manager_id = models.PositiveIntegerField(null=True, blank=True)

class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    years_of_experience = models.PositiveSmallIntegerField(null=True, blank=True)
