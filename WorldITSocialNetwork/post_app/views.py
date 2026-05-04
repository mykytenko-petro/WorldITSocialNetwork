from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostCreationForm


class PostsView(LoginRequiredMixin, FormView):
    template_name = 'post_app/posts.html'
    form_class = PostCreationForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_create'] = PostCreationForm()
        return context