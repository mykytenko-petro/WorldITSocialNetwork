from typing import Any

from django.views.generic.base import View
from django.http import HttpRequest, JsonResponse, HttpResponse

from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

from WorldITSocialNetwork.utils import PaginationProvider
from ..utils import (
    get_all_friends, get_friend_recommendations, get_friend_requests,
    add_friend_request, dismiss_recommendation, accept_friend_request, delete_friendship
)
from ..models import User


class FriendCardView(PaginationProvider):
    modes = [
        "requests",
        "recommendations",
        "all_friends",
        "home"
    ]

    def get(self, request: HttpRequest, mode: str): # type: ignore
        if not mode in self.modes:
            return HttpResponse(status=400)
        
        self.mode = mode

        return super().get(request)

    @property
    def queryset(self) -> Any:
        match self.mode:
            case "requests" | "home":
                queryset = get_friend_requests(self.request.user)

            case "recommendations":
                queryset = get_friend_recommendations(self.request.user)

            case "all_friends":
                queryset = get_all_friends(self.request.user)

        return queryset # type: ignore
    
    @property
    def template_name(self) -> str:
        return "user_app/friends/particles/user_card.html"
    
    @property
    def context(self) -> dict[str, Any]:
        return {"mode": self.mode}
    
    @property
    def per_page(self):
        if self.mode == "requests" or self.mode == "home":
            return 3    
        else:
            return 6

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

                html = render_to_string(
                    template_name="user_app/friends/particles/user_card.html",
                    context={"users": [user], "mode": "all_friends"},
                )

                return JsonResponse({
                    "html": html
                })
            case "delete":
                delete_friendship(user, other_user)
            case _:
                return JsonResponse({"message": f"wrong mode {mode}"}, status=400)

        return JsonResponse({})
