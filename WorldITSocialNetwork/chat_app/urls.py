from django.urls import path
from .views import ChatView
from .endpoints import ContactProvider

urlpatterns = [
    path('', ChatView.as_view(), name='chat_app.chat'),
    
    path('contact_provider/', ContactProvider.as_view(), name='chat_app.contact_provider')
]