from django.urls import path
from .views import ChatView
from .endpoints import (
    ContactProvider,
    ChatWithView, ChatMessagesProvider,
    CreateGroupChatView,
)


urlpatterns = [
    path('', ChatView.as_view(), name='chat_app.chat'),
    
    path('contact_provider/', ContactProvider.as_view(), name='chat_app.contact_provider'),
    
    path('chat_with/<int:user_id>/', ChatWithView.as_view(), name="chat_app.chat_with"),
    path("messages/<int:chat_id>/", ChatMessagesProvider.as_view(), name="chat_app.messages"),
    
    path('create_group_chat/', CreateGroupChatView.as_view(), name="chat_app.group_chat")
]