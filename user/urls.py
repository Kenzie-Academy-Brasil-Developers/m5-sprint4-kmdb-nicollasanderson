
from django.urls import path
from . import views as user_view
from rest_framework_simplejwt import views

urlpatterns = [
    path('users/register/', user_view.CreateUserView.as_view()),
    path('users/', user_view.GetAllUsersView.as_view()),
    path('users/<int:user_id>', user_view.GetOneUserView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
]