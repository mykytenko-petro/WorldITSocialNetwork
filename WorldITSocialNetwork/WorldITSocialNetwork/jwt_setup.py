from datetime import datetime, timedelta

import jwt
from django.views import View
from django.conf import settings
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class SocketTokenView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        token = jwt.encode(
            {
                "id": request.user.id, # type: ignore
                "iat": datetime.now(),
                "exp": datetime.now() + timedelta(days=7),
            },
            settings.JWT_SECRET,
            algorithm="HS256"
        )

        return JsonResponse({
            "token": token
        })
