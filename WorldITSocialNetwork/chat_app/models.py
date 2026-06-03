from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):
    users = models.ManyToManyField(to=User, related_name="joined_chats")

    admin = models.ForeignKey(
        to=User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="administered_chats",
    )

    name = models.CharField(max_length=30, blank=True, null=True)
    is_group = models.BooleanField(default=False)
    avatar = models.ImageField(
        upload_to="chat_app/chat_avatars/", blank=True, null=True
    )

    def __str__(self):
        return self.name or f"Chat: {self.id}"  # type: ignore


class Message(models.Model):
    readers = models.ManyToManyField(to=User, related_name="read_messages")

    sender = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    chat = models.ForeignKey(to=Chat, on_delete=models.CASCADE, related_name="messages")

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def time(self):
        return self.created_at.strftime("%H:%M")


class MessageImage(models.Model):
    message = models.ForeignKey(
        to=Message, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField()
