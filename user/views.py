from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication

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

class GetAllUsersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self,request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

class GetOneUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self,request, user_id):
        try:
            user = User.objects.filter(id=user_id)
        except User.DoesNotExist:
            return Response({'message':'user not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, many=True)

        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user:

            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})

        return Response({"detail":"invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)