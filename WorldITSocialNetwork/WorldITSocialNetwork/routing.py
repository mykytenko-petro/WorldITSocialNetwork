from django.urls import path
from channels.routing import URLRouter

import chat_app.routing
import notification_app.routing 


websocket_urlpatterns = [
    path(route='chat/', view=URLRouter(chat_app.routing.websocket_urlpatterns)),
    path(route='notifications/', view=URLRouter(notification_app.routing.websocket_urlpatterns))
]