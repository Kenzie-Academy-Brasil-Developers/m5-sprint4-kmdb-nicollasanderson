from django.db import models

# Create your models here.

class Review(models.Model):
    start = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField()
    recomendation = models.CharField(max_length=50)
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='movie')