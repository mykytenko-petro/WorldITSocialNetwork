from typing import Any

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ChatView(LoginRequiredMixin, TemplateView):
    template_name = "chat_app/chat.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["user"] = self.request.user

        return context