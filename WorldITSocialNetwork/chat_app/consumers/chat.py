import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.template.loader import render_to_string

from ..models import Chat, Message


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

        chat_info = await self.get_chat_info(self.chat_id)

        await self.send(text_data=json.dumps({
            "type": "handshake",
            "chat_id": self.chat_id,
            **chat_info
        }))

    async def send_message(self, data):
        message: Message = data.get("message")

        html = await self.async_message_render(message)

        await self.send(text_data=json.dumps({
            "type": "send_message",
            "html": html
        }))

    async def disconnect(self, code: int) -> None:
        return await super().disconnect(code)

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
    def get_other_username(self):
        user = self.scope.get("user")
        if user is None or user.is_anonymous:
            return None
        chat = Chat.objects.get(id=self.chat_id)
        other_user = chat.users.exclude(id=user.id).first()
        if other_user is None:
            return
        return other_user.username
    
    @database_sync_to_async
    def get_chat_info(self, chat_id):
        chat = Chat.objects.get(id=chat_id)

        if not chat.is_group:
            user = self.scope.get("user")
            other_user = chat.users.exclude(id=user.id).first() # type: ignore
            chat_name = other_user.username # type: ignore
        else:
            chat_name = chat.name

        return {
            "chat_name": str(chat_name),
            "chat_avatar_url": chat.avatar_url
        }
