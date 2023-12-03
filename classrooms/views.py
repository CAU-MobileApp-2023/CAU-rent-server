from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Classroom
from .serializers import ClassroomSerializer
from datetime import datetime, timedelta, time

# Create your views here.

class ClassroomList(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)

class ClassroomListInBuilding(APIView):
    def get(self, request, building):
        rooms = Classroom.objects.filter(building=building)
        serializer = ClassroomSerializer(rooms, many=True)
        return Response(serializer.data)
    
class ClassroomDetail(APIView):
    def get(self, request, building, room):
        try:
            classroom = Classroom.objects.get(building=building, room=room)
            serializer = ClassroomSerializer(classroom)
            return Response(serializer.data)
        except Classroom.DoesNotExist:
            return Response({'error': 'Classroom not found'}, status=404)

class ClassroomRegister(APIView):
    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassroomAvailability(APIView):
    def get(self, request, building, room, check_date):
        try:
            classroom = Classroom.objects.get(building=building, room=room)
            check_date = datetime.strptime(check_date, '%Y-%m-%d').date()
            
            availability = []
            for hour in range(9, 23):
                start_time = time(hour, 0)
                end_time = time(hour, 59, 59)

                is_available = classroom.check_availability(check_date, start_time, end_time)
                availability.append({
                    'time': f"{hour:02d}:00 - {hour:02d}:59",
                    'is_available': is_available
                })

            return Response(availability)
        except Classroom.DoesNotExist:
            return Response({'error': 'Classroom not found'}, status=404)
