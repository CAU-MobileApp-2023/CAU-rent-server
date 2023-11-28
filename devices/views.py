from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Device
from .serializers import DeviceSerializer

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