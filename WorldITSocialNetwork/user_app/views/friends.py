from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class FriendsView(LoginRequiredMixin, TemplateView):
    template_name = "user_app/friends/friends.html"