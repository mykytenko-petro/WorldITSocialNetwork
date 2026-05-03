from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        unique=True
    )
    email = models.EmailField(
        unique=True
    )
    author_pseudonym = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        unique=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []