from django.urls import path

from .views import ChatView
from .endpoints import (
    ContactProvider,
    ChatWithView, ChatMessagesProvider, GetChatInfoView,
    CreateGroupChatView, GroupChatProvider, EditGroupChatView,
    MessageProvider, SaveMessageView
)


urlpatterns = [
    path('', ChatView.as_view(), name='chat_app.chat'),
    
    path('contact_provider/', ContactProvider.as_view(), name='chat_app.contact_provider'),
    
    path('chat_with/<int:user_id>/', ChatWithView.as_view(), name="chat_app.chat_with"),
    path('get_chat_info/<int:chat_id>/', GetChatInfoView.as_view(), name="chat_app.get_chat_info"),
    path("messages/<int:chat_id>/", ChatMessagesProvider.as_view(), name="chat_app.messages"),
    
    path('create_group_chat/', CreateGroupChatView.as_view(), name="chat_app.group_chat"),
    path('edit_group_chat/<int:chat_id>/', CreateGroupChatView.as_view(), name="chat_app.group_chat"),
    path('group_chat_provider/', GroupChatProvider.as_view(), name="chat_app.group_chat_provider"),

    path("save_message/<int:chat_id>/", SaveMessageView.as_view(), name="chat_app.save_message"),
    path('message_chat_provider/', MessageProvider.as_view(), name="chat_app.message_chat_provider"),
]