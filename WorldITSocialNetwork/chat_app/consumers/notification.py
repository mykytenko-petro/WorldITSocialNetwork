import json
from typing import Any

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from ..models import Chat, Message


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self) -> None:
        # TODO: add validation of user

        await self.channel_layer.group_add(
            f"user_{await self.get_user_id()}",
            self.channel_name
        )
        await self.accept()
    
    async def send_notification(self, event):
        message_payload = event["message"]

        print(message_payload)

        await self.send_json({
            "event_type": "new_message",
            "data": message_payload
        })

    @database_sync_to_async
    def get_participants_ids(self, chat_id):
        chat = Chat.objects.get(id=chat_id)
        user_ids = chat.users.values_list("id", flat=True)

        return user_ids

    @database_sync_to_async
    def get_user_id(self):
        return self.scope.get("user").id # type: ignore
         