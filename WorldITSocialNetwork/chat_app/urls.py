from django.urls import path
from .views import ChatView
from .endpoints import (
    ContactProvider,
    ChatWithView, ChatMessagesProvider,
)


urlpatterns = [
    path('', ChatView.as_view(), name='chat_app.chat'),
    
    path('contact_provider/', ContactProvider.as_view(), name='chat_app.contact_provider'),
    
    path('chat_with/<int:user_id>/', ChatWithView.as_view(), name="chat_app.chat_with"),
    path("messages/<int:chat_id>/", ChatMessagesProvider.as_view(), name="chat_app.messages"),
]