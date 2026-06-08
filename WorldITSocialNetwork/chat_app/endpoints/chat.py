from typing import Any

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from WorldITSocialNetwork.utils import PaginationProvider
from user_app.utils import get_all_friends
from ..models import Chat, Message


User = get_user_model()


class ChatWithView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, user_id: int):
        other_user = get_object_or_404(User, id=user_id)
        friends = get_all_friends(request.user)

        if other_user not in friends:
            return HttpResponse(status=403)
        
        chat = Chat.objects.filter(
            is_group=False
        ).filter(
            users=request.user
        ).filter(
            users=other_user
        ).first()
        
        if not chat:
            chat = Chat.objects.create(is_group=False)
            chat.users.add(request.user, other_user)

        return JsonResponse({
            "chat_id": chat.id,  # type: ignore
            "username": other_user.username,
        })

class ChatMessagesProvider(LoginRequiredMixin, PaginationProvider):
    def get(self, request: HttpRequest, chat_id: int) -> HttpResponse: # type: ignore
        self.chat_id = chat_id
        return super().get(request)

    @property
    def queryset(self) -> Any:
        chat = get_object_or_404(
            Chat,
            id=self.chat_id
        )

        return (Message.objects
            .filter(chat=chat)
            .order_by("-id"))
    
    @property
    def template_name(self) -> str:
        return "chat_app/particles/message_card.html"

    @property
    def per_page(self) -> int:
        return 20
    
    @property
    def context(self) -> dict[str, Any]:
        return {
            "user": self.request.user
        }

# class ChatImageView(LoginRequiredMixin, View):
#     def post(self, request):
#         image = request.POST.get("image")

#         if image:
            