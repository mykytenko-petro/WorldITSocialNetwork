from django.views.generic.base import View
from django.http import HttpRequest, JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

from ..utils import (
    get_all_friends, get_friend_recommendations, get_friend_requests,
    add_friend_request, dismiss_recommendation, accept_friend_request, delete_friendship
)
from ..models import User


class FriendCardView(View):
    def post(self, request: HttpRequest):
        mode = request.POST.get("mode")
        user_count = request.POST.get("page")

        # return self.get_users(mode, int(user_count))  # type: ignore

    @staticmethod
    def get_user_cards(user: User, mode: str, page_count: int):
        match mode:
            case "requests":
                queryset = get_friend_requests(user)

            case "recommendations":
                queryset = get_friend_recommendations(user)

            case "all_friends":
                queryset = get_all_friends(user)

            case _:
                return

        if mode == "requests":
            paginator = Paginator(queryset, 3)
        else:
            paginator = Paginator(queryset, 6)

        users = paginator.get_page(page_count)

        if page_count > paginator.num_pages:
            return

        return render_to_string(
            template_name="user_app/friends/particles/user_card.html",
            context={"users": users, "mode": mode},
        )


class FriendActionView(View):
    def post(self, request: HttpRequest):        
        mode = request.GET.get("mode")

        user = request.user
        other_user = get_object_or_404(User, id=int(request.GET.get("user_id")) ) # type: ignore

        match mode:
            case "add":
                add_friend_request(user, other_user)
            case "dismiss":
                dismiss_recommendation(user, other_user)
            case "accept":
                accept_friend_request(user, other_user)
            case "delete":
                delete_friendship(user, other_user)
            case _:
                return JsonResponse({}, status=400)

        return JsonResponse({})
