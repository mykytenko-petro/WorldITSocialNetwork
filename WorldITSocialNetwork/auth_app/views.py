from django.shortcuts import render

# Create your views here.
from .forms import RegisterForm, AuthorizationForm
from django.views.generic.base import TemplateView
from .forms import AuthorizationForm, RegisterForm

class AuthorizationView(TemplateView):
    template_name = "auth_app/authorization.html"
    def get_conext_menu(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = "authorization"
        return context
    
class RegistrationView(TemplateView):
    template_name = "auth_app/registration.html"
    def get_conext_menu(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = "registration"
        return context