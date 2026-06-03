import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.template.loader import render_to_string

from .models import Chat, Message


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.chat_id: int = self.scope["url_route"]["kwargs"]["chat_id"]  # type: ignore
        self.room_group_name = f"chat_{self.chat_id}"

        username = await self.get_other_username()

        if not username:
            await self.close()
            return

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        await self.send(text_data=json.dumps({"id": self.chat_id}))

    async def receive(self, text_data):  # type: ignore
        data = json.loads(text_data)
        text = data.get("message")

        if text.strip():
            message = await self.save_message(text)

            await self.channel_layer.group_send(
                group=self.room_group_name,
                message={
                    "type": "send_message",
                    "message": message,
                }
            )

    async def send_message(self, data):
        message = data.get("message")

        html = await self.async_message_render(message)

        await self.send(text_data=json.dumps({
            "type": "send_message",
            "html": html
        }))

    @database_sync_to_async
    def async_message_render(self, message):
        return render_to_string(
            template_name="chat_app/particles/message_card.html",
            context={
                "page_obj": [message], 
                "user": self.scope.get("user")
            }
        )

    @database_sync_to_async
    def save_message(self, text):
        user = self.scope.get("user")

        new_message = Message.objects.create(
            chat_id=self.chat_id,
            sender=user,
            text=text,
        )
        return new_message

    @database_sync_to_async
    def get_other_username(self):
        user = self.scope.get("user")
        if user is None or user.is_anonymous:
            return None
        chat = Chat.objects.get(id=self.chat_id)
        other_user = chat.users.exclude(id=user.id).first()
        if other_user is None:
            return
        return other_user.username
