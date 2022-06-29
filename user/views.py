from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission
# Create your views here.

class CreateUserView(APIView):
       
    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllUsersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermission]

    def get(self,request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

class GetOneUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermission]

    def get(self,request, user_id):
        try:
            user = User.objects.filter(id=user_id)
        except User.DoesNotExist:
            return Response({'message':'user not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, many=True)

        return Response(serializer.data)
