from django.urls import path
from .views import StudentList, StudentCRUD, TeacherCRUD

urlpatterns = [
    path("student-list", StudentList.as_view(), name="student-list"),
    path(
        "student/<int:student_id>",
        StudentCRUD.as_view(),
        name="student-get-update-delete",
    ),
    path("student/", StudentCRUD.as_view(), name="student-create"),
    path("teacher/", TeacherCRUD.as_view(), name="teacher-create"),
]
