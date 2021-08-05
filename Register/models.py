from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=123)
    emp_code = models.CharField(max_length=12)
    phone = models.CharField(max_length=26)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.fullname