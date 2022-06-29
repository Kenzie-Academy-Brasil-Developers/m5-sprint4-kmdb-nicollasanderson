from pydoc import synopsis
from rest_framework import serializers
from genre.serializers import GenreSerializer
from genre.models import Genre
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField()
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        listt = validated_data['genres']

        validated_data.pop('genres')

        movie = Movie.objects.create(**validated_data)
        
        for value in listt:
            genrer = Genre.objects.get_or_create(**value)[0]
            movie.genres.add(genrer)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.premiere = validated_data.get('premiere', instance.premiere)
        instance.classification = validated_data.get('classification', instance.classification)
        instance.synopsis = validated_data.get('synopsis', instance.synopsis)
        try:
            for value in validated_data['genres']:
                genre = Genre.objects.get_or_create(**value)[0]
                instance.genres.add(genre)
        except:
            pass
        instance.save()
        return instance

