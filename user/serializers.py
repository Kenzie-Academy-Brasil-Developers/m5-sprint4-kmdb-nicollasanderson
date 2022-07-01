from django.utils import timezone
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_joined = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        
        email = User.objects.filter(email=validated_data['email'])
        
        if email:
            raise serializers.ValidationError({"email":["email already exists"]})

        validated_data['updated_at'] = timezone.now()
        validated_data['username'] = validated_data['email']

        user = User.objects.create(**validated_data)        

        user.set_password(validated_data['password'])

        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

