from rest_framework import serializers
from .models import *

class ServiceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceUser
        fields = ['email', 'name', 'student_id']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['model_name', 'model_id']

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['building', 'room']

class DeviceRentalRecordSerializer(serializers.ModelSerializer):
    renter_student_id = serializers.CharField(source='renter.student_id', write_only=True)
    renter_name = serializers.CharField(source='renter.name', write_only=True)
    device_model_name = serializers.CharField(source='device.model_name', write_only=True, allow_null=True)
    device_model_id = serializers.CharField(source='device.model_id', write_only=True, allow_null=True)

    class Meta:
        model = DeviceRentalRecord
        fields = ['renter_student_id', 'renter_name', 'device_model_name', 'device_model_id', 'start_date', 'end_date']

class ClassroomRentalRecordSerializer(serializers.ModelSerializer):
    renter_student_id = serializers.CharField(source='renter.student_id', write_only=True)
    renter_name = serializers.CharField(source='renter.name', write_only=True)
    classroom_building = serializers.CharField(source='classroom.building', write_only=True, allow_null=True)
    classroom_room = serializers.CharField(source='classroom.room', write_only=True, allow_null=True)

    class Meta:
        model = ClassroomRentalRecord
        fields = ['renter_student_id', 'renter_name', 'classroom_building', 'classroom_room', 'start_date', 'end_date']

class DeviceRentalRecordSerializer(DeviceRentalRecordSerializer):
    class Meta(DeviceRentalRecordSerializer.Meta):
        fields = ['renter', 'device', 'start_date', 'end_date']

class ClassroomRentalRecordSerializer(ClassroomRentalRecordSerializer):
    class Meta(ClassroomRentalRecordSerializer.Meta):
        fields = ['renter', 'classroom', 'start_date', 'end_date']