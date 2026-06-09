from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import get_user_model

from ..models import Chat
from user_app.utils import get_all_friends


User = get_user_model()

class CreateGroupChatView(LoginRequiredMixin, TemplateView):
    def post(self, request: HttpRequest):
        name = request.POST.get("name", "").strip()
        list_id_users = request.POST.getlist("users")

        if not name:
            return HttpResponse(status=400)
        
        list_friends_id = (
            get_all_friends(user=request.user)
            .filter(id__in=list_id_users)
            .values_list("id", flat=True)
        )

        chat = Chat.objects.create(name=name, is_group=True, admin=request.user)
        chat.users.add(request.user)
        chat.users.add(*User.objects.filter(id__in=list_friends_id))
        
        return JsonResponse({"chat_id": chat.id}) # type: ignore
