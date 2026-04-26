from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

from .forms import RegisterForm, LoginForm, ConfirmEmailForm


User = get_user_model()


class AuthTemplateView(TemplateView):
    template_name = 'user_app/auth.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['form_register'] = RegisterForm()
        context['form_login'] = LoginForm()
        context['form_confirm_email'] = ConfirmEmailForm()
        return context


class RegisterView(View):
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            return redirect('auth')

        return redirect('auth')