from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=None)
    email = models.EmailField()  # TODO:Use unique=True
    address = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=None)
    email = models.EmailField()
    salary = models.IntegerField()
    address = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True)


class Deparment(models.Model):
    department_name = models.CharField(max_length=100)
    head_of_department = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="department_headed",
    )
