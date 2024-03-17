from django.urls import path
from .views import student_list, StudentDetail

urlpatterns = [
    path("student-list", student_list, name="student-list"),
    path("student/<int:student_id>", StudentDetail.as_view(), name="student-detail"),
    path("student/", StudentDetail.as_view(), name="student-create"),
]
