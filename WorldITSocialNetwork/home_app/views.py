from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from user_app.models import User
from .forms import ProfileDetailForm
from post_app.forms import PostCreationForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home_app/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user: User = self.request.user # type: ignore
        
        if not user.profile.pseudonym or user.username == user.email: # type: ignore
            context['profile_details_form'] = ProfileDetailForm()
            
        context['post_creation_form'] = PostCreationForm()

        return context