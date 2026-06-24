from typing import override, Any

from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.html import escape
from django.db.models import Max
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from post_app.utils import compress_image
from WorldITSocialNetwork.utils import PaginationProvider
from user_app.utils import get_all_friends
from ..models import Chat, Message, MessageImage


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
    @override
    def get(self, request: HttpRequest, chat_id: int) -> HttpResponse: # type: ignore
        self.chat_id = chat_id
        return super().get(request)

    @property
    @override
    def queryset(self) -> Any:
        chat = get_object_or_404(
            Chat,
            id=self.chat_id
        )

        return (Message.objects
            .filter(chat=chat)
            .order_by("-id"))

    @property
    @override
    def per_page(self) -> int:
        return 20
    
    @override
    def render(self, page_obj):
        data = []


        for message in page_obj:
            message: Message

            # print(*[{"image": img.image.url} for img in message.images.all()]) # type: ignore

            data.append({
                "from_django": True,
                "sender_id": message.sender.id, # type: ignore
                "text": escape(message.text),
                "user_app_user": {
                    "profile_app_profile": {
                        "avatar": "", # type: ignore
                        "pseudonym": message.sender.profile.pseudonym # type: ignore
                    }
                },
                "chat_app_messageimage": [
                    {"image": img.image.url} for img in message.images.all() # type: ignore
                ]
            })

        return JsonResponse({'data': data})

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
            chat: Chat
            last_message = chat.messages.order_by('-created_at').first() # type: ignore
            
            other_user = chat.users.exclude(id=self.request.user.id).first() # type: ignore
            print(other_user)

            if last_message:
                data.append({
                    'chat_id': chat.id, # type: ignore
                    'name': escape(other_user.pseudonym), # type: ignore
                    'time': last_message.time,
                    'message_text': escape(last_message.text[:30]),

                    'user_id': other_user.id # type: ignore
                })
            else:
                data.append({
                    'chat_id': chat.id, # type: ignore
                    'name': escape(other_user.pseudonym), # type: ignore
                    'time': "",
                    'message_text': "",

                    'user_id': other_user.id # type: ignore
                })

        return JsonResponse({'data': data})
    
class SaveMessageView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, chat_id: int):
        chat = get_object_or_404(Chat, id=chat_id)
        text = request.POST.get("text", "").strip()
        images = request.FILES.getlist("images")
        print(request.POST)
        
        if not text and not images:
            print(3323)
            return HttpResponse(status=400)
        
        message = Message.objects.create(chat=chat, sender=request.user,text=text)
        
        for image in images:
            MessageImage.objects.create(
                message=message,
                image=compress_image(image)
            )
        
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)( # type: ignore
            f"chat_{chat.id}", # type: ignore
            {
                "type": "send_message",
                "message": message
            }
        )

        return HttpResponse(status=201)

class GetChatInfoView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, chat_id: int):
        chat = Chat.objects.get(id=chat_id)

        if not chat.is_group:
            user = request.user
            other_user = chat.users.exclude(id=user.id).first() # type: ignore
            chat_name = other_user.username # type: ignore
        else:
            chat_name = chat.name

        return JsonResponse({
            "chat_id": chat.id, # type: ignore
            "chat_name": str(chat_name),
            "chat_avatar_url": chat.avatar_url
        })
