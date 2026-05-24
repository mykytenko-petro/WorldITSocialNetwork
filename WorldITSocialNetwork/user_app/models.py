from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    username = models.CharField(max_length=150, blank=True, null=True, unique=True)

    email = models.EmailField(unique=True)

class Friendship(models.Model):
    status = models.CharField(max_length=50, default="pending")
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_friendships"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_friendships"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("from_user", "to_user")

    def __str__(self) -> str:
        return f"{self.from_user.username} to {self.to_user.username}"
