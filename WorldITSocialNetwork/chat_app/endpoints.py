from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string

from .models import Chat
from user_app.utils import get_all_friends

User = get_user_model()

class ChatWithView(LoginRequiredMixin, View):
    login_url = 'auth'
    
    def post(self, request, user_id, *args, **kwargs):
        other_user = User.objects.get(id=user_id)
        friends = get_all_friends(request.user)

        if other_user not in friends:
            return JsonResponse({"success": False}, status=403)

        user_id_chats = Chat.objects.filter(users=request.user, is_group=False).values_list('id', flat=True)
        chat = Chat.objects.filter(id__in=user_id_chats, users=other_user, is_group=False).first()
        if chat is None:
            chat = Chat.objects.create(is_group=False)
            chat.users.add(request.user, other_user)

        return JsonResponse({
            "success": True,
            "chat_id": chat.id,
            "username": other_user.email
        })
    
class ContactList(LoginRequiredMixin, View):
    login_url = 'auth'

    def post(self, request, *args, **kwargs):
            friends = get_all_friends(request.user)
            paginator = Paginator(friends, 10)
            
            try:
                page = paginator.page(request.GET.get("page", 1))
            except:
                return HttpResponse(status=204)

            html = ""
            for friend in page:
                html += render_to_string("chat_app/components/contact_card.html", {"friend": friend}, request=request)

            return JsonResponse({"html": html})