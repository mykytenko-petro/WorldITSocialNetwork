from django.urls import path
from .views import ChatView
from .endpoints import ContactList

urlpatterns = [
    path('', ChatView.as_view(), name='chat_app.chat'),
    path("friends/", ContactList.as_view(), name="friends-list"),
]