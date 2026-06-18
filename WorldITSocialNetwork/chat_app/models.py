from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

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

    @property
    def avatar_url(self):
        return str(self.avatar.url if self.avatar else "/static/chat_app/icon/new-group.svg")

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
        local_datetime = timezone.localtime(self.created_at)
        
        return local_datetime.strftime("%H:%M")
    
    def __str__(self) -> str:
        if not self.text:
            self.text = ""

        return self.text if len(self.text) < 20 else self.text[:20] + "..."


class MessageImage(models.Model):
    message = models.ForeignKey(
        to=Message, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField()
