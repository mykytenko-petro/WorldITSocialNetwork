from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostsView(LoginRequiredMixin, TemplateView):
    template_name = 'post_app/posts.html'