from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(required=False)
    email = serializers.EmailField(required=False)
    address = serializers.CharField(required=False, allow_blank=True)
    profile_image = serializers.ImageField(required=False, allow_null=True)

    def to_representation(self, instance):
        data = {
            "name": instance.name,
            "date_of_birth": instance.date_of_birth,
            "email": instance.email,
            "address": instance.address,
            "profile_image": instance.profile_image.url
            if instance.profile_image
            else None,
        }
        return data
