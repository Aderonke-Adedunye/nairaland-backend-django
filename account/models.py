from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# Create your models here.


class User(AbstractUser):
    photo = models.ImageField(upload_to="profile")
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []