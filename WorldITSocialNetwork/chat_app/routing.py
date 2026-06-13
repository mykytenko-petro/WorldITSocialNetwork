from django.urls import path
from .consumers import ChatConsumer, NotificationConsumer


websocket_urlpatterns = [
    path("<int:chat_id>/", ChatConsumer.as_asgi()), # type: ignore
    path("notifications/", NotificationConsumer.as_asgi()) # type: ignore
]