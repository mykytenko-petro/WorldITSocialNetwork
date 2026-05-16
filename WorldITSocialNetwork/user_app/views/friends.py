from typing import Any

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..endpoints import FriendCardView

class FriendsView(LoginRequiredMixin, TemplateView):
    template_name = "user_app/friends/friends.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["requests_cards"] = FriendCardView.get_user_cards("requests", 1)

        return context