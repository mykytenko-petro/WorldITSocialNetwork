from django.views.generic.base import TemplateView
from typing import Any
from django.shortcuts import render
from .forms import RegisterForm, LoginForm, ConfirmEmailForm

class AuthTemplateView(TemplateView):
    template_name = 'user_app/auth.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form_register'] = RegisterForm()
        context['form_register'].label_suffix = ""
        context['form_login'] = LoginForm()
        context['form_login'].label_suffix = ""
        context['form_confirm_email'] = ConfirmEmailForm()
        context['form_confirm_email'].label_suffix = ""
        return context


