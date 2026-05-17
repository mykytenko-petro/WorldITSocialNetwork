from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.http import HttpRequest, JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from ..utils import (
    get_all_friends,
    get_friend_recommendations,
    get_friend_requests
)
from ..models import User


class FriendCardView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest):
        mode = request.POST.get("mode")
        user_count = request.POST.get('page')

        # return self.get_users(mode, int(user_count))  # type: ignore
    
    @staticmethod
    def get_user_cards(user: User, mode: str, page_count: int):
        # TODO: create and use user query utils instead of hardcoded all users

        match mode:
            case "requests":
                queryset = get_friend_requests(user)

            case "recommendations":
                queryset = get_friend_recommendations(user)

            case "all_friends":
                queryset = get_all_friends(user)

            case _:
                return 
            
        paginator = Paginator(queryset, 3)
        users = paginator.get_page(page_count)
        
        if page_count > paginator.num_pages:
            return 
        
        return render_to_string(
            template_name="user_app/friends/particles/user_card.html",
            context={
                "users": users,
                "mode": mode
            }
        )