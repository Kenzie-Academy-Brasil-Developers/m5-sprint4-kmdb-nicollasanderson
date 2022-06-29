from functools import partial
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user import serializers

from .serializers import MovieSerializer
from .models import Movie

from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import MoviePermission
# Create your views here.

class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviePermission]

    def get(self, request):
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleMovieView(APIView):
    def get(self,request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({'message':'movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self,request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie, request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def delete(self, request, movie_id):
        get_object_or_404(Movie, id=movie_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
