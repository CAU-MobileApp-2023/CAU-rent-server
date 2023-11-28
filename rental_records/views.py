from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RentalRecord
from .serializers import RentalRecordSerializer, DeviceRentalRecordSerializer, ClassroomRentalRecordSerializer

class RentalRecordList(APIView):
    def get(self, request):
        records = RentalRecord.objects.all()
        serializer = RentalRecordSerializer(records, many=True)
        return Response(serializer.data)

class RentalRecordListByStudentId(APIView):
    def get(self, request, student_id):
        records = RentalRecord.objects.filter(renter__student_id=student_id)
        serializer = RentalRecordSerializer(records, many=True)
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
