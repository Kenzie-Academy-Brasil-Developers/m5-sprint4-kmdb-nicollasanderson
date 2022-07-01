from django.urls import path
from . import views as user_view

urlpatterns = [
    path('movies/<int:movie_id>/review/', user_view.ReviewView.as_view()),
    path('reviews/<int:review_id>',user_view.DeleteReviewView.as_view()),
    path('reviews/',user_view.GetAllReviewsView.as_view())
]