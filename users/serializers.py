from rest_framework import serializers
from .models import ServiceUser

class ServiceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceUser
        fields = ['email', 'password', 'name', 'student_id', 'phone_number', 'department']