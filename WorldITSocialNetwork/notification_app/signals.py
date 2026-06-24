from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils.html import escape

from chat_app.models import Message


@receiver(post_save, sender=Message)
def broadcast_message_to_participants(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()

        chat = instance.chat
        user_ids = chat.users.exclude(id=instance.sender.id).values_list("id", flat=True)

        if chat.is_group:
            chat_name = chat.name
        else:
            chat_name = instance.sender.pseudonym

        for user_id in user_ids:
            async_to_sync(channel_layer.group_send)( # type: ignore
                f"user_{user_id}",
                {
                    "type": "send_notification",
                    "message": {
                        "type": "message_send",

                        "is_group": chat.is_group,

                        'chat_id': chat.id,
                        'name': escape(chat_name),
                        'time': instance.time,
                        'message_text': escape(instance.text[:30])
                    }
                }
            )