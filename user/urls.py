
from django.urls import path
from . import views as user_view
from rest_framework.authtoken import views

urlpatterns = [
    path('users/register/', user_view.UserView.as_view()),
    path('users/login/', views.obtain_auth_token)
]