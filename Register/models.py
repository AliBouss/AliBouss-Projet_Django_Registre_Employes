from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=123)


class Employee(models.Model):
    fullname = models.CharField(max_length=123)
    emp_code = models.CharField(max_length=12)
    phone = models.CharField(max_length=26)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)