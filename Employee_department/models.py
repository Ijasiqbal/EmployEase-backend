from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    managerId = models.PositiveIntegerField(null=True, blank=True)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    contactNumber = models.CharField(max_length=15, null=True, blank=True)
    dateOfJoining = models.DateField(null=True, blank=True)
    yearsOfExperience = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)