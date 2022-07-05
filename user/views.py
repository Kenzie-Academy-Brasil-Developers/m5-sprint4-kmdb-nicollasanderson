from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from .models import User
from .serializers import LoginSerializer, UserSerializer

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

class GetAllUsersView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self,request):
        users = User.objects.all()

        result_page = self.paginate_queryset(users, request, view=self)

        serializer = UserSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

class GetOneUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self,request, user_id):
        try:
            user = User.objects.filter(id=user_id)
        except User.DoesNotExist:
            return Response({'message':'user not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, many=True)

        return Response(serializer.data[0])

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        verify = serializer.is_valid()

        if not verify:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if user:

            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})

        return Response({"detail":"invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)