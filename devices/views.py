from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Device
from .serializers import DeviceSerializer
from datetime import datetime, timedelta, time

# Create your views here.

class DeviceList(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

class DeviceListByModelName(APIView):
    def get(self, request, model_name):
        devices = Device.objects.filter(model_name=model_name)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

class DeviceDetail(APIView):
    def get(self, request, model_name, model_id):
        try:
            device = Device.objects.get(model_name=model_name, model_id=model_id)
            serializer = DeviceSerializer(device)
            return Response(serializer.data)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found'}, status=404)
        
class DeviceRegister(APIView):
    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceAvailability(APIView):
    def get(self, request, model_name, model_id):
        try:
            device = Device.objects.get(model_name=model_name, model_id=model_id)
            today = datetime.today()
            dates = [today + timedelta(days=i) for i in range(31)]

            availability = []
            for date in dates:
                # 대여 시작 시간을 오전 9시로 설정
                start_of_day = datetime.combine(date, time(9, 0))
                # 대여 종료 시간을 오후 6시로 설정
                end_of_day = datetime.combine(date, time(18, 0))

                is_available = device.check_availability(start_of_day, end_of_day)
                availability.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'time_range': f"{start_of_day.strftime('%H:%M')} - {end_of_day.strftime('%H:%M')}",
                    'is_available': is_available
                })

            return Response(availability)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found'}, status=404)