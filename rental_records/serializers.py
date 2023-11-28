from rest_framework import serializers
from .models import ServiceUser, Device, Classroom, RentalRecord

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

class RentalRecordSerializer(serializers.ModelSerializer):
    renter_student_id = serializers.CharField(source='renter.student_id', read_only=True)
    renter_name = serializers.CharField(source='renter.name', read_only=True)
    device_model_name = serializers.CharField(source='device.model_name', read_only=True, allow_null=True)
    classroom_building = serializers.CharField(source='classroom.building', read_only=True, allow_null=True)
    classroom_room = serializers.CharField(source='classroom.room', read_only=True, allow_null=True)

    class Meta:
        model = RentalRecord
        fields = ['renter_student_id', 'renter_name', 'device_model_name', 'classroom_building', 'classroom_room', 'start_date', 'end_date']

class DeviceRentalRecordSerializer(RentalRecordSerializer):
    class Meta(RentalRecordSerializer.Meta):
        fields = ['renter', 'device', 'start_date', 'end_date']

class ClassroomRentalRecordSerializer(RentalRecordSerializer):
    class Meta(RentalRecordSerializer.Meta):
        fields = ['renter', 'classroom', 'start_date', 'end_date']
