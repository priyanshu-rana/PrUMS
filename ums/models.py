from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    profile_image = models.ImageField()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    profile_image = models.ImageField()
    salary = models.IntegerField()


class Deparment(models.Model):
    department_name = models.CharField(max_length=100)
    head_of_department = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="department_headed",
    )
