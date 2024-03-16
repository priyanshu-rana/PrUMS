from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer


def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)
