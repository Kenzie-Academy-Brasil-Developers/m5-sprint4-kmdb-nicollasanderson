from django.urls import path, include

from . import views

urlpatterns = [
    path('movies/',views.MovieView.as_view()),
    path('movies/<int:movie_id>/', views.SingleMovieView.as_view()),
]