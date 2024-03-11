from django.contrib import admin
from .models import Student, Teacher, Deparment


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_of_birth", "email", "address")


@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_of_birth", "email", "address", "salary")


@admin.register(Deparment)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "department_name", "head_of_department")
