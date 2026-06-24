from typing import Any

from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from ..utils import (
    get_all_friends, get_friend_recommendations, get_friend_requests,
)
from user_app.models import User


class FriendsView(LoginRequiredMixin, TemplateView):
    template_name = "user_app/friends/friends.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        current_user = self.request.user

        context["requests_cards"] = self._get_user_cards(current_user, "requests", 1)
        context["recommendation_cards"] = self._get_user_cards(current_user, "recommendations", 1)
        context["friends_cards"] = self._get_user_cards(current_user, "all_friends", 1)

        return context
    
    def _get_user_cards(self, user, mode: str, page_count: int):
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
            context={"page_obj": users, "mode": mode},
        )

class FriendPageView(LoginRequiredMixin, TemplateView):
    template_name = "user_app/friends/friend_page.html"

    def get(self, request, user_id, *args, **kwargs):
        target_user = get_object_or_404(User, id=user_id)
        context = self.get_context_data(**kwargs)
        context["target_user"] = target_user
        return self.render_to_response(context)