from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout
from django.shortcuts import redirect

from ..forms import RegisterForm, LoginForm, ConfirmEmailForm


class AuthView(UserPassesTestMixin, TemplateView):
    template_name = 'user_app/auth/auth.html'

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('home_app.index')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        context['form_register'] = RegisterForm()
        context['form_login'] = LoginForm()
        context['form_confirm_email'] = ConfirmEmailForm()

        return context

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user_app.auth')