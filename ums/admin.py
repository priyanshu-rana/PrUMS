from django.contrib import admin
from .models import Student, Teacher, Deparment


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = {"id", "name", "age", "email", "address"}
