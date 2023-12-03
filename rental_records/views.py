from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.utils import timezone

class DeviceRentalRecordList(APIView):
    def get(self, request):
        records = DeviceRentalRecord.objects.all()
        serializer = DeviceRentalRecordSerializer(records, many=True)
        return Response(serializer.data)

class ClassroomRentalRecordList(APIView):
    def get(self, request):
        records = ClassroomRentalRecord.objects.all()
        serializer = ClassroomRentalRecordSerializer(records, many=True)
        return Response(serializer.data)

class DeviceRentalRecordListByStudentId(APIView):
    def get(self, request, student_id):
        records = DeviceRentalRecord.objects.filter(renter__student_id=student_id)
        serializer = DeviceRentalRecordSerializer(records, many=True)
        return Response(serializer.data)

class ClassroomRentalRecordListByStudentId(APIView):
    def get(self, request, student_id):
        records = ClassroomRentalRecord.objects.filter(renter__student_id=student_id)
        serializer = ClassroomRentalRecordSerializer(records, many=True)
        return Response(serializer.data)    

class RentDevice(APIView):
    def post(self, request):
        serializer = DeviceRentalRecordSerializer(data=request.data)
        if serializer.is_valid():
            rental_record = serializer.save()
            return Response({
                'message': 'Device rented successfully',
                'rental_record': DeviceRentalRecordSerializer(rental_record).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentClassroom(APIView):
    def post(self, request):
        serializer = ClassroomRentalRecordSerializer(data=request.data)
        if serializer.is_valid():
            rental_record = serializer.save()
            return Response({
                'message': 'Classroom rented successfully',
                'rental_record': ClassroomRentalRecordSerializer(rental_record).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentalRecordListOfDevice(APIView):
    def get(self, request, model_name, model_id):
        records = DeviceRentalRecord.objects.filter(device__model_name=model_name, device__model_id=model_id)
        serializer = DeviceRentalRecordSerializer(records, many=True)
        return Response(serializer.data)

class RentalRecordListOfClassroom(APIView):
    def get(self, request, building, room):
        records = ClassroomRentalRecord.objects.filter(classroom__building=building, classroom__room=room)
        serializer = ClassroomRentalRecordSerializer(records, many=True)
        return Response(serializer.data)

class NowDeviceRentalRecordListByStudentId(APIView):
    def get(self, request, student_id):
        now = timezone.now()

        print(now)

        records = DeviceRentalRecord.objects.filter(
            renter__student_id=student_id,
            start_date__lte=now, 
            end_date__gte=now
        )
        serializer = DeviceRentalRecordSerializer(records, many=True)
        return Response(serializer.data)

class NowClassroomRentalRecordListByStudentId(APIView):
    def get(self, request, student_id):
        now = timezone.now()
        records = ClassroomRentalRecord.objects.filter(
            renter__student_id=student_id,
            start_date__lte=now, 
            end_date__gte=now
        )
        serializer = ClassroomRentalRecordSerializer(records, many=True)
        return Response(serializer.data)