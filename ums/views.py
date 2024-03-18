from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer, StudentUpdateSerializer


def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)


class StudentCRUD(APIView):
    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        serializer = StudentUpdateSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
