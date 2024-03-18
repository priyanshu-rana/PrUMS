from django.urls import path
from .views import student_list, Student

urlpatterns = [
    path("student-list", student_list, name="student-list"),
    path(
        "student/<int:student_id>", Student.as_view(), name="student-get-update-delete"
    ),
    path("student/", Student.as_view(), name="student-create"),
]
