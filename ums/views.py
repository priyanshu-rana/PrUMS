from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from .models import Student
from .serializers import StudentSerializer, StudentUpdateSerializer

logger = logging.getLogger(__name__)


class StudentList(APIView):
    def get(self, request):
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

    def delete(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
            student.delete()
            return Response(
                {"message": "Student deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Student.DoesNotExist:
            return Response(
                {"error": "Student does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(
                f"An unexpected error occurred while deleting the student: {str(e)}"
            )
            return Response(
                {"error": "An unexpected error occurred while deleting the student"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
