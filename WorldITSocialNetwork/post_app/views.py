from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostCreationForm


class PostsView(LoginRequiredMixin, TemplateView):
    template_name = 'post_app/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_creation_form'] = PostCreationForm()

        return context