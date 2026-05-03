from django.views.generic.base import TemplateView
from user_app.forms import ProfileDetailForm
from django.contrib.auth.mixins import LoginRequiredMixin

from user_app.models import User


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home_app/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user: User = self.request.user # type: ignore
        
        if not user.author_pseudonym or user.username != ' ':
            context['profile_details_form'] = ProfileDetailForm()
            
        return context