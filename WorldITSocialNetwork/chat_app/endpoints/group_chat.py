from typing import Any, override

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from django.utils.html import escape

from WorldITSocialNetwork.utils import PaginationProvider

from ..models import Chat
from user_app.utils import get_all_friends

User = get_user_model()


class CreateGroupChatView(LoginRequiredMixin, TemplateView):
    def post(self, request: HttpRequest):
        name = request.POST.get("name", "").strip()
        list_id_users = request.POST.getlist("users")

        # TODO: make friends validation

        if not name:
            return HttpResponse(status=400)

        # list_friends_id = (
        #     get_all_friends(user=request.user)
        #     .filter(id__in=)
        #     .values_list("id", flat=True)
        # )

        chat = Chat.objects.create(name=name, is_group=True, admin=request.user)
        chat.users.add(request.user)
        chat.users.add(*User.objects.filter(id__in=list_id_users))

        return JsonResponse({"chat_id": chat.id})  # type: ignore

class GroupChatProvider(LoginRequiredMixin, PaginationProvider):
    @property
    @override
    def queryset(self) -> Any:
        return Chat.objects.filter(users=self.request.user, is_group=True)
    
    @property
    @override
    def template_name(self) -> str:
        return ""
    
    def render(self, page_obj):
        data = []

        for chat in page_obj:
            last_message = chat.messages.order_by('-created_at').first()

            if last_message:
                data.append({
                    'chat_id': chat.id,
                    'timestamp': last_message.created_at,
                    'name': escape(chat.name),
                    'time': last_message.time,
                    'message_text': escape(last_message.text[:30])
                })
            else:
                data.append({
                    'chat_id': chat.id,
                    'timestamp': "",
                    'name': escape(chat.name),
                    'time': "",
                    'message_text': ""
                })

        return JsonResponse({'data': data})