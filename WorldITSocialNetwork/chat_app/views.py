from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from .models import Chat
from user_app.utils import get_all_friends


User = get_user_model()

class ChatView(
        LoginRequiredMixin,
        # FormView, 
        TemplateView
    ):
    template_name = "chat_app/chat.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["friends"] = get_all_friends(self.request.user) # type: ignore
        # context["personal_chats"] = Chat.objects.filter(users= self.request.user, is_group= False).order_by("id")
        
        return context