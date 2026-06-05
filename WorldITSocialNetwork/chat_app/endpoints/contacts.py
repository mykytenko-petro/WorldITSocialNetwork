from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin

from WorldITSocialNetwork.utils import PaginationProvider
from user_app.utils import get_all_friends


class ContactProvider(LoginRequiredMixin, PaginationProvider):
    @property
    def queryset(self) -> Any:
        return get_all_friends(self.request.user)

    @property
    def template_name(self) -> str:
        return "chat_app/particles/contact_card.html"