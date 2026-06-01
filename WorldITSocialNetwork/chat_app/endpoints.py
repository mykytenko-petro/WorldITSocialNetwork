from typing import Any

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from WorldITSocialNetwork.utils import PaginationProvider
from user_app.utils import get_all_friends
from .models import Chat


User = get_user_model()

class ChatWithView(LoginRequiredMixin, View):
    login_url = 'auth'
    
    def post(self, request, user_id, *args, **kwargs):
        other_user = User.objects.get(id= user_id)
        friends = get_all_friends(request.user)

        if other_user not in friends:
            return JsonResponse({"success": False}, status= 403)

        user_id_chats = Chat.objects.filter(users= request.user, is_group= False).values_list('id', flat= True)
        chat = Chat.objects.filter(id__in= user_id_chats, users= other_user, is_group= False).first()
        if chat is None:
            chat = Chat.objects.create(is_group= False)
            chat.users.add(request.user, other_user)
        return JsonResponse(
            {
                "success": True,
                "chat_id": chat.id, # type: ignore
                "username": other_user.email
            }
        )

class ChatProvider(LoginRequiredMixin, PaginationProvider):
    @property
    def queryset(self) -> Any:
        return get_all_friends(self.request.user)
    
    @property
    def template_name(self) -> str:
        return super().template_name