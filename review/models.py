from django.db import models

# Create your models here.

class RecomendationsChoices(models.TextChoices):
    MUSTWATCH = ("MW", "Must Watch")
    SHOULDWATCH = ("SW", "Should Watch")
    AVOIDWATCH = ("AW", "Avoid Watch")
    NOOPINION = ("NO", "No Opinion")

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField()
    critic = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='critic', default='')
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='movie')
    recomendation = models.CharField(max_length=50, choices=RecomendationsChoices.choices,default=RecomendationsChoices.NOOPINION)