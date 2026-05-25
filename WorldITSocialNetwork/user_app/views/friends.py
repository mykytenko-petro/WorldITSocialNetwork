from typing import Any

from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..endpoints import FriendCardView

from user_app.utils.friends import accept_friend_request, delete_friendship
from user_app.models import User


class FriendsView(LoginRequiredMixin, TemplateView):
    template_name = "user_app/friends/friends.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        current_user = self.request.user

        context["requests_cards"] = FriendCardView.get_user_cards(current_user, "requests", 1)  # type: ignore
        context["recommendation_cards"] = FriendCardView.get_user_cards(current_user, "recommendations", 1)  # type: ignore
        context["friends_cards"] = FriendCardView.get_user_cards(current_user, "all_friends", 1)  # type: ignore

        return context

class FriendPageView(LoginRequiredMixin, TemplateView):
    template_name = "user_app/friends/friend_page.html"

    def get(self, request, user_id, *args, **kwargs):
        target_user = get_object_or_404(User, id=user_id)
        context = self.get_context_data(**kwargs)
        context["target_user"] = target_user
        return self.render_to_response(context)