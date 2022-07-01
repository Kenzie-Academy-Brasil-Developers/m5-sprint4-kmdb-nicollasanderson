import email
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movie.models import Movie
from review.models import Review
from review.permissions import ReviewPermission
from review.serializers import ReviewSerializer
from rest_framework.authentication import TokenAuthentication
from user.models import User
from .permissions import DeleteReviewPermission

class ReviewView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewPermission]
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({'message':"movie not found"}, status=status.HTTP_404_NOT_FOUND)

        reviews = Review.objects.filter(movie_id=movie.id)

        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data)

    def post(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({'message':"movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(movie=movie, critic=request.user)

        return Response(serializer.data)

class DeleteReviewView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DeleteReviewPermission]

    def delete(self,request, review_id):
        get_object_or_404(Review, id=review_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetAllReviewsView(APIView):
    def get(self,request):
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data)