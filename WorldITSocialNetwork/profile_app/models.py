from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    author_pseudonym = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        unique=True
    )