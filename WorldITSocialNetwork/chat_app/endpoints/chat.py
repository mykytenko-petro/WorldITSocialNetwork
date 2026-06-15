from typing import override, Any

from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.html import escape
from django.db.models import Max


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
    
class CreateMessageChatView(LoginRequiredMixin, TemplateView):
    def post(self, request: HttpRequest):
        name = request.POST.get("name", "").strip()
        # TODO: make friends validation

        if not name:
            return HttpResponse(status=400)

        # list_friends_id = (
        #     get_all_friends(user=request.user)
        #     .filter(id__in=)
        #     .values_list("id", flat=True)
        # )

        return JsonResponse({"chat_id": chat.id})  # type: ignore

class MessageProvider(LoginRequiredMixin, PaginationProvider):
    @property
    @override
    def queryset(self) -> Any:
        return Chat.objects.filter(
            users=self.request.user,
            is_group=False
        ).annotate(
            last_message_at=Max('messages__created_at')
        ).order_by('-last_message_at')
    
    @override
    def render(self, page_obj):
        data = []

        for chat in page_obj:
            last_message = chat.messages.order_by('-created_at').first()
            
            other_user = chat.users.exclude(id=self.request.user.id).first() # type: ignore
            print(other_user)

            if last_message:
                data.append({
                    'chat_id': chat.id,
                    'name': escape(other_user.pseudonym),
                    'time': last_message.time,
                    'message_text': escape(last_message.text[:30])
                })
            else:
                data.append({
                    'chat_id': chat.id,
                    'name': escape(other_user.pseudonym),
                    'time': "",
                    'message_text': ""
                })

        return JsonResponse({'data': data})
    
# class SaveMessageView(LoginRequiredMixin, View):
#     def post(self, request: HttpRequest, chat_id: int, *args, **kwargs):
#         chat = get_object_or_404(Chat, id=chat_id, users=request.user)
#         text = request.POST.get("text", "").strip()
#         images = request.FILES.getlist("images")
        
#         if not text and not images:
#             return JsonResponse({
#                 {"error": "empty"}
#             })