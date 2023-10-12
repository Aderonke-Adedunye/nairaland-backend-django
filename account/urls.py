from django.urls import path 
from .views import signup, Login

urlpatterns = [
    path("signup/", signup),
    path("login/", Login)
]