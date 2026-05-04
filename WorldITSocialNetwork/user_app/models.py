from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        unique=True
    )
    
    email = models.EmailField(
        unique=True
    )