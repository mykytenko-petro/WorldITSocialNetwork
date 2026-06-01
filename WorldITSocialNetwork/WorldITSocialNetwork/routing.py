from django.urls import path
from channels.routing import URLRouter
from chat_app.routing import websocket_urlpatterns

websocket_urlpatterns = [
    path(route='chat/', view=URLRouter(websocket_urlpatterns)),
]