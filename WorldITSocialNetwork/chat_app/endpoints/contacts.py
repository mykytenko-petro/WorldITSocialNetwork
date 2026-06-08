import email
from typing import Any, override
import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.html import escape

from WorldITSocialNetwork.utils import PaginationProvider
from user_app.utils import get_all_friends
from user_app.models import User


class ContactProvider(LoginRequiredMixin, PaginationProvider):
    @property
    @override
    def queryset(self) -> Any:
        # test
        # real = list(get_all_friends(self.request.user))

        # fake = [
        #     User(username=secrets.token_hex(10), email=i, id=i)
        #     for i in range(100)
        # ]

        # return real + fake
        return get_all_friends(self.request.user)

    @property
    @override
    def template_name(self) -> str:
        return "chat_app/particles/contact_card.html"
    
    @property
    @override
    def per_page(self) -> int:
        return 15

    @override
    def render(self, page_obj):
        data = []

        for contact in page_obj:
            data.append({
                "user_id": contact.id,
                "pseudonym": escape(contact.username),
                # TODO: add image
            })

        return JsonResponse({"data": data})