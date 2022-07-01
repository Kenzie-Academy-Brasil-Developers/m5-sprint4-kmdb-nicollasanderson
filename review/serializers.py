from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from movie.models import Movie
from movie.serializers import MovieSerializer

from user.serializers import UserSerializer
from user.models import User
from .models import Review

class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name']

class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id','critic','stars','review','spoilers','recomendation','movie_id']

    def validate_stars(self, stars):
        if stars < 0:
            raise serializers.ValidationError("Ensure this value is less than or equal to 10.")
        elif stars > 10:
            raise serializers.ValidationError("Ensure this value is less than or equal to 10.")

        return stars