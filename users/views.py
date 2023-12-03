from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceUser
from .serializers import ServiceUserSerializer

# Create your views here.

class UserList(APIView):
    def get(self, request):
        users = ServiceUser.objects.all()
        serializer = ServiceUserSerializer(users, many=True)
        return Response(serializer.data)
    
class UserDetail(APIView):
    def get(self, request, student_id):
        try:
            user = ServiceUser.objects.get(student_id=student_id)
            serializer = ServiceUserSerializer(user)
            return Response(serializer.data)
        except ServiceUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class UserSignUp(APIView):
    def post(self, request):
        user_data = request.data
        
        new_user = ServiceUser(
            email=user_data['email'],
            name=user_data['name'],
            student_id=user_data['student_id'],
            phone_number=user_data['phone_number'],
            department=user_data['department'],
            password=user_data['password']
        )
        
        new_user.save()

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class UserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = ServiceUser.objects.get(email=email)
        except ServiceUser.DoesNotExist:
            return Response({'error': 'Email does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if user.password == password:
            user_data = {
                'email': user.email,
                'name': user.name,
                'student_id': user.student_id,
            }
            return Response({'message': 'Successfully login', 'user_data': user_data}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
        
class UserLogout(APIView):
    def post(self, request):
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)