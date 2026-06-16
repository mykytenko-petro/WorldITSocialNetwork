from typing import Any, override

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from django.utils.html import escape
from django.db.models import Max
from django.shortcuts import get_object_or_404

from WorldITSocialNetwork.utils import PaginationProvider

from ..models import Chat

User = get_user_model()


class CreateGroupChatView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest):
        name = request.POST.get("name", "").strip()
        list_id_users = request.POST.getlist("users")
        avatar_file = request.FILES.get("avatar")

        # TODO: make friends validation

        if not name:
            return HttpResponse(status=400, content="Group name is required.")

        chat = Chat.objects.create(name=name, is_group=True, admin=request.user)
        
        if avatar_file:
            chat.avatar = avatar_file # type: ignore
            chat.save()

        chat.users.add(request.user)
        chat.users.add(*User.objects.filter(id__in=list_id_users))

        return JsonResponse({"chat_id": chat.id})  # type: ignore


class EditGroupChatView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, chat_id: int):
        name = request.POST.get("name", "").strip()
        list_id_users = request.POST.getlist("users")
        avatar_file = request.FILES.get("avatar")

        # TODO: make friends validation

        if not name:
            return HttpResponse(status=400, content="Group name is required.")

        chat = get_object_or_404(Chat, id=chat_id, admin=request.user)
        
        chat.name = name
        if avatar_file:
            chat.avatar = avatar_file # type: ignore
        chat.save()

        new_users = User.objects.filter(id__in=list_id_users)
        chat.users.set(list(new_users) + [request.user])

        return JsonResponse({"chat_id": chat.id})  # type: ignore


class GroupChatProvider(LoginRequiredMixin, PaginationProvider):
    @property
    @override
    def queryset(self) -> Any:
        return Chat.objects.filter(
            users=self.request.user,
            is_group=True
        ).annotate(
            last_message_at=Max('messages__created_at')
        ).order_by('-last_message_at')
    
    @override
    def render(self, page_obj):
        data = []

        for chat in page_obj:
            last_message = chat.messages.order_by('-created_at').first()

            if last_message:
                data.append({
                    'chat_id': chat.id,
                    'name': escape(chat.name),
                    'time': last_message.time,
                    'message_text': escape(last_message.text[:30])
                })
            else:
                data.append({
                    'chat_id': chat.id,
                    'name': escape(chat.name),
                    'time': "",
                    'message_text': ""
                })

        return JsonResponse({'data': data})
    