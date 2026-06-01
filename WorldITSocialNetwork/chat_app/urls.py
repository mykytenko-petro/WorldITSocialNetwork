from django.urls import path
from .views import ChatView
from .endpoints import ChatProvider

urlpatterns = [
    path('', ChatView.as_view(), name='chat_app.chat'),
    path('chat_provider/', ChatProvider.as_view(), name='chat_app.chat_provider')
]