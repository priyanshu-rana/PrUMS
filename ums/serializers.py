from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "date_of_birth", "email", "address", "profile_image"]


class StudentUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    date_of_birth = serializers.DateField(required=False)
    address = serializers.CharField(required=False)
    profile_image = serializers.ImageField(required=False)

    class Meta:
        model = Student
        fields = ["id", "name", "date_of_birth", "email", "address", "profile_image"]
