from django.urls import path
from chat_app.consumers import ChatConsumer


websocket_urlpatterns = [
    path("<int:chat_id>/", ChatConsumer.as_asgi()), # type: ignore
]